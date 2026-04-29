# P_ADM_SUBS_GLOBAL_USER_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Aggregates and deduplicates historical user subscription data for a specified month (`P_YYYYMM`). It performs validation on source data availability, then creates or refreshes a monthly partition in the `CLM_ADM.ADM_SUBS_GLOBAL_USER_HIST` table by processing data into a temporary table and performing a partition exchange.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
- ← [[CLM_ADM.ADM_GLOBAL_USER_SUBS_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| COMOYO_USER_ID |
| SUBSCRIPTION_ID |
| MIN_SKY_NO_DAYS_FIRST_USE |
- ← [[CLM_ADM.ADM_CONNECT_ID_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CONNECT_ID |
| SUBSCRIPTION_ID |
- ← [[CLM_ADM.ADM_SUBS_GLOBAL_USER_HIST]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_SUBS_GLOBAL_USER_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| COMOYO_USER_ID |
| MIN_SKY_NO_DAYS_FIRST_USE |
- → [[CLM_ADM.TMP_SUBS_GLOBAL_USER_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| COMOYO_USER_ID |
| MIN_SKY_NO_DAYS_FIRST_USE |

