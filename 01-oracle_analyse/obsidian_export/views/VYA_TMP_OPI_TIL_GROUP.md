# VYA_TMP_OPI_TIL_GROUP

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates aggregated monthly metrics for customer events related to a specific application or service (e.g., Mitt Telenor mobile app configuration), including unique days loaded, sessions, and users, for the previous month.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| FIRST_DATE_KEY |
| LAST_DATE_KEY |
- ← [[CCDW_CUSTOMER_EVENT.CUSTOMER_EVENT_DETAIL]]
| Column Name |
|---|
| EVENT_DATE_ID |
| SOURCE_SYSTEM_ID |
| KURT_ID_EVENT |
| EVENT_MEDIUM_ID |
| EVENT_TYPE_ID |
- ← [[CCDW_CUSTOMER_EVENT.EVENT_MEDIUM]]
| Column Name |
|---|
| SOURCE_SYSTEM_ID |
| EVENT_MEDIUM_ID |
| EVENT_MEDIUM_DESC |

