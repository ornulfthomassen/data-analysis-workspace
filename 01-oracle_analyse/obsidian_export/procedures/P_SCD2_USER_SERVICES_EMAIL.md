# P_SCD2_USER_SERVICES_EMAIL

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Implements a Type 2 Slowly Changing Dimension (SCD2) for user service email data. It processes daily incremental updates from source data (COMOYO.USER_SERVICES_EMAIL), identifying new active user emails, existing active user emails, and emails that have become inactive. The procedure updates the main SCD2 table (SCD2_USER_SERVICES_EMAIL) by creating two temporary tables (one for current records, one for past/historical records) and then atomically swapping them into the respective partitions of the SCD2 table.

## Data Sources (Inputs)
- ← [[COMOYO.USER_SERVICES_EMAIL]]
| Column Name |
|---|
| FILE_DATE |
| USER_ID |
| EMAIL |
- ← [[SCD2_USER_SERVICES_EMAIL]]
| Column Name |
|---|
| LAST_DATE |
| USER_ID |
| EMAIL |
| FIRST_DATE |
| LAST_DATE |
| CURRENT_RECORD |

## Target Tables (Outputs)
- → [[SCD2_USER_SERVICES_EMAIL]]
| Column Name |
|---|
| USER_ID |
| EMAIL |
| FIRST_DATE |
| LAST_DATE |
| CURRENT_RECORD |
- → [[TMP_SCD2_USER_SERVICES_E_C_REC]]
| Column Name |
|---|
| USER_ID |
| EMAIL |
| FIRST_DATE |
| LAST_DATE |
| CURRENT_RECORD |
- → [[TMP_SCD2_USER_SERVICES_E_P_REC]]
| Column Name |
|---|
| USER_ID |
| EMAIL |
| FIRST_DATE |
| LAST_DATE |
| CURRENT_RECORD |

