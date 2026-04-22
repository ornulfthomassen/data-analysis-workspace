# KIM_CUSTOMER_RESPONSE_VA

**Schema:** `CCM` | **Type:** `View`

## Description
This view enriches customer response transaction data with descriptive information about response types and communication channels. Its primary function is to rank customer responses for each contact, prioritizing them based on a predefined response importance (lower `RESPONSE_RANK` indicating higher priority) and then by recency (`RESPONSE_DTTM` descending). This allows for easy identification of the most relevant or important recent responses for a given customer.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CUSTOMER_RESPONSE]]
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]
- ← [[CRM_ANALYSE.KIM_CHANNEL_DIM]]

