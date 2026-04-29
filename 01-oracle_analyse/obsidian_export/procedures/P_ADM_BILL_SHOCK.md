# P_ADM_BILL_SHOCK

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Processes mobile traffic data for a specified month, calculating aggregated 'bill shock' metrics (total NOK, twin count) per subscriber and main number. It creates a temporary table with these aggregated results, dynamically manages a partition in the target 'bill shock' analysis table, and then exchanges the temporary table into the appropriate partition of the permanent table. It includes checks for existing tables and partitions and handles overwrite conditions.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
| SUBOBJECT_NAME |
- ← [[CLM_ADM.ADM_BILL_SHOCK]]
- ← [[CLM_ADM.ADM_MOBILE_TRAFFIC_AGG]]
| Column Name |
|---|
| SUBSCR_ID |
| MAIN_NUMBER_HOVED |
| MAIN_NUMBER_BRUKT |
| NOK |
| GENEVA_CALL_TYPE |
| PERIOD_MONTH_KEY |
- ← [[ADM_SUBSCRIPTION_MASTER_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SUBSCR_ID_NUM |

## Target Tables (Outputs)
- → [[CLM_ADM.TMP_BILL_SHOCK]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| NOK |
| ANTALL_TWIN |
- → [[CLM_ADM.ADM_BILL_SHOCK]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| NOK |
| ANTALL_TWIN |

