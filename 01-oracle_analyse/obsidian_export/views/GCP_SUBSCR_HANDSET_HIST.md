# GCP_SUBSCR_HANDSET_HIST

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `GCP_SUBSCR_HANDSET_HIST`, serves to expose historical subscription handset data from the `CLM_ADM` schema into the `CCM` schema. It provides a direct, untransformed mirror of the underlying table, including details such as period, subscription ID, TAC (Type Allocation Code), model ID, and the first and last dates of terminal use. The 'GCP' prefix might indicate its intended use in Google Cloud Platform-related data processes.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBSCR_HANDSET_HIST]]

