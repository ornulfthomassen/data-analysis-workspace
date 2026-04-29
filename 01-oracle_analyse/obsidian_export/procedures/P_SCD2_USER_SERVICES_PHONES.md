# P_SCD2_USER_SERVICES_PHONES

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure implements a Slowly Changing Dimension Type 2 (SCD2) logic for user services phone data. It incrementally processes new daily records from `COMOYO.USER_SERVICES_PHONES` to update and maintain a historical record of user phone numbers in the `SCD2_USER_SERVICES_PHONES` table. For each new `FILE_DATE`, it identifies active records that remain unchanged, newly active records, and previously active records that are now inactive, and updates the `SCD2_USER_SERVICES_PHONES` table using partition exchange with temporary tables (`TMP_SCD2_USER_SERVICES_P_C_REC` and `TMP_SCD2_USER_SERVICES_P_P_REC`) to reflect these changes over time.

## Data Sources (Inputs)
- ← [[COMOYO.USER_SERVICES_PHONES]]
| Column Name |
|---|
| FILE_DATE |
| USER_ID |
| PHONES |
- ← [[SCD2_USER_SERVICES_PHONES]]
| Column Name |
|---|
| LAST_DATE |
| USER_ID |
| PHONES |
| FIRST_DATE |
| CURRENT_RECORD |

## Target Tables (Outputs)
- → [[TMP_SCD2_USER_SERVICES_P_C_REC]]
| Column Name |
|---|
| USER_ID |
| PHONES |
| FIRST_DATE |
| LAST_DATE |
| CURRENT_RECORD |
- → [[TMP_SCD2_USER_SERVICES_P_P_REC]]
| Column Name |
|---|
| USER_ID |
| PHONES |
| FIRST_DATE |
| LAST_DATE |
| CURRENT_RECORD |
- → [[SCD2_USER_SERVICES_PHONES]]
| Column Name |
|---|
| USER_ID |
| PHONES |
| FIRST_DATE |
| LAST_DATE |
| CURRENT_RECORD |

