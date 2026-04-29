# P_SCD2_USER_SERVICES_SERVICE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Implements a Type 2 Slowly Changing Dimension (SCD2) for user service access data. It processes daily changes from the source `COMOYO.USER_SERVICES_SERVICE` table, identifying new, changed, and unchanged records. These records are then aggregated into temporary tables which are subsequently swapped into the 'CURRENT_REC' and 'PAST_REC' partitions of the main `SCD2_USER_SERVICES_SERVICE` table using partition exchange, effectively maintaining a history of user service access records.

## Data Sources (Inputs)
- ← [[COMOYO.USER_SERVICES_SERVICE]]
| Column Name |
|---|
| LAST_ACCESS_TM |
| USER_ID |
| SERVICE_NAME |
| FIRST_ACCESS_TM |
- ← [[SCD2_USER_SERVICES_SERVICE]]
| Column Name |
|---|
| LAST_DATE |
| USER_ID |
| SERVICE_NAME |
| FIRST_ACCESS_TM |
| LAST_ACCESS_TM |
| FIRST_DATE |
| CURRENT_RECORD |
| ON_LAST_FILE |

## Target Tables (Outputs)
- → [[TMP_SCD2_USER_SERVICES_S_C_REC]]
| Column Name |
|---|
| USER_ID |
| SERVICE_NAME |
| FIRST_ACCESS_TM |
| LAST_ACCESS_TM |
| FIRST_DATE |
| LAST_DATE |
| ON_LAST_FILE |
| CURRENT_RECORD |
- → [[TMP_SCD2_USER_SERVICES_S_P_REC]]
| Column Name |
|---|
| USER_ID |
| SERVICE_NAME |
| FIRST_ACCESS_TM |
| LAST_ACCESS_TM |
| FIRST_DATE |
| LAST_DATE |
| ON_LAST_FILE |
| CURRENT_RECORD |
- → [[SCD2_USER_SERVICES_SERVICE]]
| Column Name |
|---|
| USER_ID |
| SERVICE_NAME |
| FIRST_ACCESS_TM |
| LAST_ACCESS_TM |
| FIRST_DATE |
| LAST_DATE |
| ON_LAST_FILE |
| CURRENT_RECORD |

