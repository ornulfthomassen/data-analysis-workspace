# GCP_SUBSCRIPTION_HANDSET

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a curated list of current or active subscription handset details. It selects various attributes related to subscriptions and their associated handsets. Key transformations include casting `SUBSCRIPTION_KEY` to a VARCHAR2 for `SUBSCRIPTION_ID`, and applying complex `CASE` logic to derive `SUB_NUMBER`, which appears to handle specific historical data anomalies or special conditions (e.g., flagging records where `MAIN_NUMBER` equals `SUB_NUMBER` with '-2'). The view specifically filters for current records by checking `TERMINAL_USE_LAST_DATE = DATE'9999-12-31'` and positive `SUBSCRIPTION_KEY` values.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCRIPTION_HANDSET_DIM_V]]

