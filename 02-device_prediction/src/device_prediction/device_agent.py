"""LLM-based device features enrichment using Gemini 2.5 Pro with Google Search.

Calls Gemini to look up device specifications (RAM, storage, camera, price, etc.)
for mobile phone models found in subscription data. Includes retry logic, JSON
validation, and batch processing with concurrent workers.
"""

from __future__ import annotations

import json
import logging
import re
from concurrent.futures import ThreadPoolExecutor

import pandas as pd
from pydantic import BaseModel, field_validator
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

from device_prediction import bq_client
from device_prediction.config import Settings

logger = logging.getLogger(__name__)

# System instruction for Gemini (from POC notebook)
SYSTEM_INSTRUCTION = """You are an expert in the mobile phone industry, specializing in historical and current device analysis. Your primary task is to categorize and extract relevant features for specific mobile phone models based on their release year and market context. Your output must be optimized for direct ingestion into a BigQuery table, meaning all extracted features should be top-level keys in the JSON object.

Follow these rules strictly:
1.  **Input Parsing:** The user will provide the 'device_name' and 'manufacturer'. You must independently determine the 'release_year' for the specified device name and manufacturer. This 'release_year' is critical for all subsequent analysis.
2.  **Contextual Awareness:** When evaluating a phone, always consider its determined 'release_year'. A 'premium' phone from 2013 must be evaluated against other phones from 2013, not current standards.
3.  **Categorization:** Provide a 'device_series_annual' category for the phone, choosing from: 'Ultra-Premium Flagship', 'Premium Flagship', 'High-End', 'Mid-Range', 'Budget', 'Entry-Level'. If uncertain, state 'Uncategorized'.
4.  **Feature Extraction - Explicit Keys:** Extract the following key technical specifications. Each must be its own top-level key in the JSON output, with a precise value:
    *   **`ram_gb`**: RAM capacity in GB (e.g., 2, 4, 6, 8, 12, 16). If multiple, use the most common/base model.
    *   **`storage_base_gb`**: Base internal storage capacity in GB (e.g., 16, 32, 64, 128, 256, 512, 1024).
    *   **`display_type`**: Primary display technology (e.g., 'Super AMOLED', 'OLED', 'LCD', 'IPS LCD').
    *   **`display_size_inches`**: Display size in inches (e.g., 5.0, 6.1, 6.7).
    *   **`camera_rear_mp`**: Megapixels of the primary rear camera (e.g., 12, 48, 108, 200).
    *   **`camera_front_mp`**: Megapixels of the primary front camera (e.g., 5, 10, 12).
5.  **Price Conversion:** For the 'launch_price', always provide it in NOK (Norwegian Kroner) as the key `launch_price_nok`. If the original launch price is found in another currency, convert it to NOK based on the approximate exchange rate at the time of the phone's release year. State the converted value as a numerical string (e.g., "6000", "12500").
6.  **Context Summary:** Provide a 'context_summary' that briefly explains the phone's market position, key selling points, and relevance in its launch year.
7.  **Conciseness:** Provide direct answers and avoid conversational filler unless explicitly asked.
8.  **Output Format:** Always provide your response in a structured JSON format. Ensure the JSON includes the following top-level keys in this exact order: `device_name`, `manufacturer`, `release_year`, `device_series_annual`, `ram_gb`, `storage_base_gb`, `display_type`, `display_size_inches`, `camera_rear_mp`, `camera_front_mp`, `launch_price_nok`, `context_summary`. All values should be precise.
9.  **Language:** Respond in Norwegian if the user's prompt is in Norwegian, otherwise use English.
10. **User input:** Input Parsing string shall be included as a top-level key in the JSON output.
11. **device_name** Manufacturer should not be included in the device_name.
12. **device_series_annual** Should be one of the following: 'Ultra-Premium Flagship', 'Premium Flagship', 'Flagship' 'High-End', 'Mid-Range', 'Budget', 'Entry-Level'. Example iphone 16 pro max should be categorized as Ultra-Premium Flagship, iphone 16 pro as Premium Flagship, iphone 16 as flagship, iphone se as Mid-Range.
13. **Generation** Should be a number that is defined by the number in its device_series_annual.
14. **device_series_annual_no** Should be a number coresponding to the device_series_annual by these rules excactly: when device_series_annual = 'Uncategorized' then 99
when device_series_annual = 'Entry-Level' then 1
when device_series_annual = 'Budget' then 2
when device_series_annual = 'Mid-Range' then 3
when device_series_annual = 'High-End' then 4
when device_series_annual = 'Flagship' then 5
when device_series_annual = 'Premium Flagship' then 6
when device_series_annual = 'Ultra-Premium Flagship' then 7
{
"""


class DeviceFeatures(BaseModel):
    """Validated device features schema matching the BigQuery device_features table."""

    user_input: str
    device_name: str
    manufacturer: str
    release_year: str | None = None
    ram_gb: str | None = None
    storage_base_gb: str | None = None
    display_type: str | None = None
    display_size_inches: str | None = None
    camera_rear_mp: str | None = None
    camera_front_mp: str | None = None
    launch_price_nok: str | None = None
    device_series_annual: str | None = None
    device_series_annual_no: int | None = None
    generation: int | None = None
    context_summary: str | None = None

    @field_validator("device_name", "manufacturer", mode="before")
    @classmethod
    def uppercase_strings(cls, v: str) -> str:
        return str(v).upper() if v else v

    @field_validator("release_year", mode="before")
    @classmethod
    def coerce_release_year_to_string(cls, v: object) -> str | None:
        if v is None or v == "":
            return None
        return str(int(float(str(v))))

    @field_validator("generation", mode="before")
    @classmethod
    def coerce_to_int(cls, v: object) -> int | None:
        if v is None or v == "":
            return None
        try:
            return int(float(str(v)))
        except (ValueError, TypeError):
            return None

    @field_validator("ram_gb", "storage_base_gb", "display_size_inches",
                     "camera_rear_mp", "camera_front_mp", "launch_price_nok",
                     mode="before")
    @classmethod
    def coerce_numeric_to_string(cls, v: object) -> str | None:
        if v is None or v == "" or v == "None":
            return None
        try:
            # Handle strings like "6,990" or "12 500"
            cleaned = str(v).replace(",", "").replace(" ", "")
            # Convert to float first to validate, then to string
            numeric = float(cleaned)
            # Return as string, removing unnecessary decimals
            if numeric == int(numeric):
                return str(int(numeric))
            return str(numeric)
        except (ValueError, TypeError):
            return None


def find_missing_devices(cfg: Settings) -> pd.DataFrame:
    """Query BigQuery to find devices not yet in the device_features table.

    Returns DataFrame with column 'user_input' containing
    UPPER(producer + ' ' + marketing_name) for each missing device.
    """
    bq = cfg.bigquery
    agent = cfg.device_agent
    device_type_list = ", ".join(f"'{dt}'" for dt in cfg.extraction.device_types)

    query = f"""
    SELECT DISTINCT UPPER(t1.manufacturer || ' ' || t1.marketing_name) AS user_input
    FROM (
        SELECT
            device_producername AS manufacturer,
            device_marketing_name AS marketing_name,
            COUNT(DISTINCT customer_sk_user) AS max_footprint
        FROM `{bq.subscription_hist_table}`
        WHERE device_type IN ({device_type_list})
            AND period_month_date IS NOT NULL
        GROUP BY ALL
    ) AS t1
    WHERE UPPER(TRIM(t1.manufacturer || ' ' || t1.marketing_name)) NOT IN (
        SELECT UPPER(TRIM(user_input))
        FROM `{bq.device_features_table}`
        WHERE user_input IS NOT NULL
    )
    AND max_footprint >= {agent.min_device_footprint}
    """

    df = bq_client.read_query(query, bq.project_id)
    logger.info("Found %d missing devices to enrich", len(df))
    return df


def call_gemini(device_name: str, cfg: Settings) -> str:
    """Call Gemini 2.5 Pro with Google Search grounding.

    Retries up to max_retries times with exponential backoff.
    """
    from google import genai
    from google.genai import types

    @retry(
        stop=stop_after_attempt(cfg.device_agent.max_retries),
        wait=wait_exponential(multiplier=2, min=2, max=30),
        retry=retry_if_exception_type((Exception,)),
        before_sleep=lambda rs: logger.warning(
            "Retry %d for '%s': %s", rs.attempt_number, device_name, rs.outcome.exception()
        ),
    )
    def _call() -> str:
        client = genai.Client(
            vertexai=True,
            project=cfg.device_agent.vertex_ai_project,
            location=cfg.device_agent.vertex_ai_location,
        )

        contents = [
            types.Content(
                role="user",
                parts=[types.Part(text=device_name)],
            )
        ]

        config = types.GenerateContentConfig(
            temperature=0.5,
            top_p=0.95,
            seed=0,
            max_output_tokens=3000,
            system_instruction=[types.Part(text=SYSTEM_INSTRUCTION)],
        )

        response = client.models.generate_content(
            model=cfg.device_agent.model_name,
            contents=contents,
            config=config,
        )
        return response.text

    return _call()


def parse_device_response(raw_response: str, user_input: str) -> DeviceFeatures:
    """Parse LLM response into validated DeviceFeatures.

    Handles:
    1. Strip markdown fencing (```json ... ```)
    2. Fix common JSON issues (trailing commas, unescaped quotes)
    3. Flatten nested 'features' dict if present
    4. Validate via Pydantic model
    """
    json_str = raw_response

    # Strip markdown code fencing
    if "```json" in json_str:
        json_str = json_str.split("```json")[1].split("```")[0]
    elif "```" in json_str:
        json_str = json_str.split("```")[1].split("```")[0]

    json_str = json_str.strip()

    # Fix trailing commas before closing braces/brackets
    json_str = re.sub(r",\s*([}\]])", r"\1", json_str)

    data = json.loads(json_str)

    # Flatten nested 'features' dict if the LLM returned it that way
    if "features" in data and isinstance(data["features"], dict):
        features = data.pop("features")
        data.update(features)

    # Force user_input to match the original query
    data["user_input"] = user_input

    # Normalize keys to lowercase
    data = {k.lower().replace(" ", "_"): v for k, v in data.items()}

    return DeviceFeatures(**data)


def enrich_single_device(device_name: str, cfg: Settings) -> DeviceFeatures | None:
    """End-to-end: call LLM, parse, validate for one device.

    Returns None on failure after retries are exhausted.
    """
    try:
        raw = call_gemini(device_name, cfg)
        return parse_device_response(raw, device_name)
    except Exception as e:
        logger.error("Failed to enrich '%s': %s", device_name, e)
        return None


def enrich_devices_batch(
    devices_df: pd.DataFrame,
    cfg: Settings,
) -> pd.DataFrame:
    """Process devices in batches with concurrent workers.

    Each batch is written to BigQuery immediately after processing.
    Returns DataFrame of all successfully enriched devices.
    """
    agent = cfg.device_agent
    device_names = devices_df["user_input"].tolist()
    all_results: list[pd.DataFrame] = []

    for batch_start in range(0, len(device_names), agent.batch_size):
        batch = device_names[batch_start : batch_start + agent.batch_size]
        batch_num = batch_start // agent.batch_size + 1
        total_batches = (len(device_names) + agent.batch_size - 1) // agent.batch_size
        logger.info("Processing batch %d/%d (%d devices)", batch_num, total_batches, len(batch))

        with ThreadPoolExecutor(max_workers=agent.max_workers) as executor:
            results = list(executor.map(
                lambda name: enrich_single_device(name, cfg), batch
            ))

        successful = [r for r in results if r is not None]
        failed = len(batch) - len(successful)

        if successful:
            batch_df = pd.DataFrame([r.model_dump() for r in successful])
            all_results.append(batch_df)

            # Write batch to BigQuery immediately
            bq_client.write_dataframe(
                batch_df,
                cfg.bigquery.device_features_table,
                cfg.bigquery.project_id,
                write_disposition="WRITE_APPEND",
            )
            logger.info("Batch %d: %d successful, %d failed", batch_num, len(successful), failed)
        else:
            logger.warning("Batch %d: all %d devices failed", batch_num, len(batch))

    if all_results:
        return pd.concat(all_results, ignore_index=True)
    return pd.DataFrame()
