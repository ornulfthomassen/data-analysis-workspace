# TMP_CUSTOMER_STATUS

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `TMP_CUSTOMER_STATUS`, extracts and transforms specific customer status information. It selects the period month key and customer key, and translates customer status codes ('K' for 'Levende' (Alive), 'UD' for 'Død' (Dead)) into more descriptive Norwegian names, with a default 'UKJENT' (Unknown). The data is filtered to include only certain customer types ('PU', 'P', 'PC') and specific customer status codes ('K', 'UD'), while excluding a predefined list of customer SKs. The view serves as an intermediary step, indicated by the comment 'BRUKES TIL LASTING TIL Viya' (used for loading to Viya), suggesting it prepares customer status data for an analytical platform.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]

