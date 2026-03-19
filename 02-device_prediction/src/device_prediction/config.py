"""Configuration management. Loads YAML config with environment variable overrides."""

from __future__ import annotations

from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel
from pydantic_settings import BaseSettings

_DEFAULT_CONFIG = Path(__file__).resolve().parents[2] / "config" / "default.yaml"


class BigQueryConfig(BaseModel):
    project_id: str = "tnn-consumer-common-nx"
    dataset: str = "DataScience"
    subscription_hist_table: str = "tnn-consumer-common-nx.ADM.subscription_hist"
    subscription_master_table: str = (
        "tnn-consumer-common-nx-gold.Dimensions.subscription_master_history"
    )
    device_features_table: str = "tnn-consumer-common-nx.DataScience.device_features"
    score_output_dataset: str = "tnn-consumer-common-nx-gold.datascience"
    score_output_prefix: str = "device_change_score"


class ExtractionConfig(BaseModel):
    device_types: list[str] = [
        "PDA", "CLAMSHELL", "SMARTPHONE", "BLOCK", "SLIDER", "RUGGED",
    ]
    train_sample_rate: float = 0.4
    train_history_years: int = 3
    train_buffer_months: int = 2


class CleaningConfig(BaseModel):
    max_days_after_release: int = 730
    min_device_usage_days: int = 30


class StatisticsConfig(BaseModel):
    gen_stat_lookback_months: int = 13


class TargetConfig(BaseModel):
    max_horizon_months: int = 36


class ModelConfig(BaseModel):
    type: Literal["gradient_boosted_survival", "xgboost_aft"] = (
        "gradient_boosted_survival"
    )
    n_estimators: int = 100
    learning_rate: float = 0.1
    max_depth: int = 4
    test_size: float = 0.2
    random_state: int = 42


class DeviceAgentConfig(BaseModel):
    vertex_ai_project: str = "tnn-pnx-consumer-common-ai"
    vertex_ai_location: str = "europe-west1"
    model_name: str = "gemini-2.5-pro"
    batch_size: int = 10
    max_workers: int = 5
    max_retries: int = 3
    min_device_footprint: int = 500


class Settings(BaseSettings):
    bigquery: BigQueryConfig = BigQueryConfig()
    extraction: ExtractionConfig = ExtractionConfig()
    cleaning: CleaningConfig = CleaningConfig()
    statistics: StatisticsConfig = StatisticsConfig()
    target: TargetConfig = TargetConfig()
    model: ModelConfig = ModelConfig()
    device_agent: DeviceAgentConfig = DeviceAgentConfig()

    model_config = {"env_prefix": "DP_", "env_nested_delimiter": "__"}


def load_config(config_path: str | Path | None = None) -> Settings:
    """Load settings from YAML file, with environment variable overrides."""
    path = Path(config_path) if config_path else _DEFAULT_CONFIG

    if path.exists():
        with open(path) as f:
            data = yaml.safe_load(f) or {}
        return Settings(**data)

    return Settings()
