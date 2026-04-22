# V_ADM_CONNECT_ID_CUST_HIST

**Schema:** `CCM` | **Type:** `View`

## Description
Retrieves historical customer connection data, specifically period month key, customer surrogate key, and connect ID. It performs a data cleansing step by replacing a customer surrogate key value of -1 with NULL, likely to standardize or handle missing/unknown customer references.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CONNECT_ID_CUST_HIST]]

