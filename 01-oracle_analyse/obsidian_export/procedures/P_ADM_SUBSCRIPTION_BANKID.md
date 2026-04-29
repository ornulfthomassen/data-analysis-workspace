# P_ADM_SUBSCRIPTION_BANKID

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure calculates and aggregates BankID usage statistics for subscriptions over a three-month period relative to a specified month (P_YYYYMM). It validates the availability of source data, creates a new partition in the 'ADM_SUBSCRIPTION_BANKID' table if it doesn't exist, populates a temporary table with the calculated data, and then exchanges this temporary table with the new partition. The process includes logging its execution status and handles various error conditions.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[CONAX.FACT_BANKID]]
| Column Name |
|---|
| FK_DATE |
| OPERATION_TIME |
| NUMBER_OF_TRANSACTIONS |
| FK_ENDUSER_ID |
- ← [[CONAX.DIM_ENDUSER]]
| Column Name |
|---|
| PK_ENDUSER_ID |
| MSISDN |
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| FIRST_DATE |
| LAST_DATE |
| PERIOD_MONTH_KEY |
- ← [[CLM_ADM.ADM_MOB_SUBSCRIPTION_CORE]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| END_DATE |
| ORIGINAL_START_DATE |
| MAIN_NUMBER |
- ← [[ADM_SUBSCRIPTION_BANKID]]

## Target Tables (Outputs)
- → [[ADM_SUBSCRIPTION_BANKID]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| BANKID_USED_LAST1 |
| BANKID_USED_LAST2 |
| BANKID_USED_LAST3 |
- → [[TMP_SUBSCRIPTION_BANKID]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| BANKID_USED_LAST1 |
| BANKID_USED_LAST2 |
| BANKID_USED_LAST3 |
- → [[CRM_ANALYSE.ADM_LOAD_HISTORY]]
| Column Name |
|---|
| TABLE_NAME |
| PERIOD_YYYYMM |
| STATUS |
| MESSAGE |

