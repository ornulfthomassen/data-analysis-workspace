# ADM_SUBSCR_HANDSET_HIST_AGG_V

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates historical handset usage data for each unique subscription and model ID. It identifies the first and last recorded period of use, the overall first and last terminal usage dates, and captures the initial and final states of various handset attributes (such as producer, model name, OS type, category, touch screen, device type, HD voice, and LTE capabilities) based on the monthly period key. It excludes a specific model ID from the aggregation.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBSCR_HANDSET_HIST]]

