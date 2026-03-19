# Device Change Prediction

## Project Overview
Survival analysis model predicting time-to-device-change for mobile subscribers. Replaces a POC with duplicated SQL scripts and manual Colab notebooks with a modular Python package.

## Architecture
```
src/device_prediction/
├── config.py          # Pydantic settings from config/default.yaml + env overrides
├── bq_client.py       # BigQuery read/write wrapper (Application Default Credentials)
├── extract.py         # Parameterized SQL extraction (train/score mode), runs server-side in BQ
├── device_history.py  # Multi-pass device timeline cleaning (pandas). Core business logic.
├── statistics.py      # 3 aggregation levels: subscriber, market, device-model
├── features.py        # Feature matrix assembly (joins + seasonal + computed features)
├── target.py          # Survival target: (duration_months, event) with censoring
├── encoding.py        # sklearn ColumnTransformer (replaces hardcoded SQL CASE one-hot)
├── model.py           # scikit-survival GradientBoostingSurvivalAnalysis
├── device_agent.py    # Gemini 2.5 Pro + Google Search for device spec enrichment
├── pipeline.py        # Orchestration with step-by-step execution + parquet intermediates
└── cli.py             # CLI: device-prediction step-{enrich,extract,...} or train/score
```

## Key Conventions
- **Python-first**: BigQuery is only used for extraction (source tables too large for local). All transformation in pandas.
- **Shared pipeline**: Train and score use identical extract → clean → stats → features logic. Mode parameter controls differences.
- **Intermediate files**: Each step saves to `data/intermediate/*.parquet` for inspection.
- **Config-driven**: All thresholds, table names, model params in `config/default.yaml`.
- **No one-hot in SQL**: Producer encoding is dynamic via sklearn OneHotEncoder.

## Data Sources (BigQuery)
- `tnn-consumer-common-nx.ADM.subscription_hist` - monthly subscription snapshots
- `tnn-consumer-common-nx-gold.Dimensions.subscription_master_history` - subscription → main_number_sk mapping
- `tnn-consumer-common-nx.DataScience.device_features` - LLM-enriched device specs

## Running
```bash
# Step-by-step (recommended for verification)
device-prediction step-enrich
device-prediction step-extract --mode train
device-prediction step-device-history --mode train
device-prediction step-statistics --mode train
device-prediction step-features --mode train
device-prediction step-target
device-prediction step-encode --mode train
device-prediction step-train

# Full pipeline
device-prediction train
device-prediction score --model-path models/latest
```

## Testing
```bash
python3 -m pytest tests/ -v
```

## POC Reference
Original prototype files in `POC/` directory. Key differences from POC:
- Survival analysis instead of binary classification
- No SQL duplication (was 90% identical between ABT and prediction scripts)
- Dynamic encoding instead of 20 hardcoded CASE WHEN blocks
- Device agent has retry logic, Pydantic validation, batch processing
