# VYA_ADM_ORDEN_ACTIVATION

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides the latest 'ORDEN' activation details and related metrics, such as activation flags, availability dates, first activation dates, and days waited for activation, linked to a customer surrogate key. It retrieves this information from historical activation data, filtered for the most recent snapshot, and then maps it to customer keys.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_ORDEN_ACTIVATION_HIST]]
| Column Name |
|---|
| KURT_ID |
| SIGNUP_DATE |
| START_FROM_DATE |
| LAST_FOREGROUND_TIME |
| DATE_ID |
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_KEY |

