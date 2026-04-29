"""Delt konfigurasjon og hjelpefunksjoner for Oracle-analyse."""

import json
import os
import time

import pandas as pd
import vertexai
from google.cloud import bigquery
from vertexai.preview.generative_models import GenerativeModel

# --- Konstanter ---

VERTEX_AI_PROJECT = "tnn-pnx-consumer-common-ai"
VERTEX_AI_LOCATION = "europe-west1"
MODEL_NAME = "gemini-2.5-flash"
BIGQUERY_PROJECT = "tnn-consumer-common-nx"
BQ_DATASET = "temp"

# --- Skjemaregister ---

SCHEMAS = {
    "ccm": {
        "views_table": "ccm_user_views",
        "source_table": "ccm_user_source",
    },
    "clm_adm": {
        "views_table": "clm_adm_user_views",
        "source_table": "clm_adm_user_source",
    },
    "clm_ccm": {
        "views_table": "clm_ccm_user_views",
        "source_table": "clm_ccm_user_source",
    },
    "crm_analyse": {
        "views_table": "crm_analyse_user_views",
        "source_table": "crm_analyse_user_source",
    },
}


def get_full_table_id(schema: str, obj_type: str) -> str:
    """Konstruerer fullt kvalifisert BigQuery-tabell-ID.

    Args:
        schema: Skjemanavn (f.eks. 'ccm', 'clm_adm')
        obj_type: 'views' eller 'procedures'
    """
    key = "views_table" if obj_type == "views" else "source_table"
    table_name = SCHEMAS[schema][key]
    return f"{BIGQUERY_PROJECT}.{BQ_DATASET}.{table_name}"


def get_output_filename(schema: str, obj_type: str, output_dir: str = ".") -> str:
    """Konstruerer outputfilnavn som matcher eksisterende navnekonvensjon."""
    table_id = get_full_table_id(schema, obj_type)
    safe_name = table_id.replace(".", "_").replace("/", "_")
    suffix = "views_analysis" if obj_type == "views" else "procedures_analysis"
    return os.path.join(output_dir, f"{safe_name}_{suffix}.json")


def get_checkpoint_filename(schema: str, obj_type: str, output_dir: str = ".") -> str:
    """Konstruerer checkpoint-filnavn."""
    table_id = get_full_table_id(schema, obj_type)
    safe_name = table_id.replace(".", "_").replace("/", "_")
    suffix = "views_checkpoint" if obj_type == "views" else "procedures_checkpoint"
    return os.path.join(output_dir, f"{safe_name}_{suffix}.json")


# --- GCP-funksjoner ---


def check_gcp_auth():
    """Sjekker at GCP Application Default Credentials er gyldige."""
    try:
        client = bigquery.Client(project=BIGQUERY_PROJECT)
        # Kjør en enkel query for å verifisere
        list(client.query("SELECT 1").result())
        print("GCP-autentisering OK")
    except Exception as e:
        print(f"GCP-autentisering feilet: {e}")
        print("Kjør: gcloud auth application-default login")
        raise SystemExit(1)


def init_vertex_ai() -> GenerativeModel:
    """Initialiserer Vertex AI og returnerer Gemini-modell."""
    vertexai.init(project=VERTEX_AI_PROJECT, location=VERTEX_AI_LOCATION)
    return GenerativeModel(MODEL_NAME)


def fetch_bigquery_data(table_id: str) -> pd.DataFrame:
    """Henter alle rader fra en BigQuery-tabell."""
    client = bigquery.Client(project=BIGQUERY_PROJECT)
    query = f"SELECT * FROM `{table_id}`"
    print(f"Henter data fra {table_id}...")
    df = client.query(query).to_dataframe()
    print(f"Lastet {len(df)} rader.")
    return df


# --- LLM-funksjoner ---


def parse_llm_response(response_text: str) -> dict:
    """Fjerner markdown-fences og parser JSON fra LLM-respons."""
    text = response_text.strip()
    if text.startswith("```json") and text.endswith("```"):
        text = text[7:-3].strip()
    elif text.startswith("```") and text.endswith("```"):
        text = text[3:-3].strip()
    return json.loads(text)


def call_llm_with_retry(model: GenerativeModel, prompt: str, max_retries: int = 3) -> str:
    """Kaller Gemini med retry og backoff ved feil."""
    for attempt in range(max_retries):
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            if attempt < max_retries - 1:
                wait = 30 * (attempt + 1)
                print(f"  LLM-feil (forsøk {attempt + 1}/{max_retries}): {e}")
                print(f"  Venter {wait}s før nytt forsøk...")
                time.sleep(wait)
            else:
                raise


# --- Checkpoint-funksjoner ---


def load_checkpoint(checkpoint_path: str) -> tuple[set, list]:
    """Laster checkpoint-fil. Returnerer (fullførte_navn, resultater)."""
    if os.path.exists(checkpoint_path):
        with open(checkpoint_path, "r") as f:
            data = json.load(f)
        completed = set(data.get("completed", []))
        results = data.get("results", [])
        print(f"Lastet checkpoint: {len(completed)} allerede analysert")
        return completed, results
    return set(), []


def save_checkpoint(checkpoint_path: str, completed: set, results: list):
    """Lagrer checkpoint atomisk (via temp-fil)."""
    tmp_path = checkpoint_path + ".tmp"
    data = {"completed": list(completed), "results": results}
    with open(tmp_path, "w") as f:
        json.dump(data, f, indent=2)
    os.replace(tmp_path, checkpoint_path)


def cleanup_checkpoint(checkpoint_path: str):
    """Sletter checkpoint-fil etter vellykket gjennomføring."""
    if os.path.exists(checkpoint_path):
        os.remove(checkpoint_path)
        print("Checkpoint ryddet opp.")
