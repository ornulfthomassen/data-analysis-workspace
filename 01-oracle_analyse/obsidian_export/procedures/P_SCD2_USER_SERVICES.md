# P_SCD2_USER_SERVICES

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure implements a Slowly Changing Dimension (SCD) Type 2 strategy for user services data. It processes new daily snapshots of user services from 'COMOYO.USER_SERVICES', identifies changes, and updates the 'SCD2_USER_SERVICES' table by maintaining a full history of changes. It does this by creating temporary tables for current and past records based on the latest data, and then exchanging these temporary tables with the corresponding partitions ('CURRENT_REC' and 'PAST_REC') of the main 'SCD2_USER_SERVICES' table.

## Data Sources (Inputs)
- ← [[COMOYO.USER_SERVICES]]
| Column Name |
|---|
| FILE_DATE |
| USER_ID |
- ← [[SCD2_USER_SERVICES]]
| Column Name |
|---|
| LAST_DATE |
| USER_ID |
| FIRST_DATE |
| CURRENT_RECORD |
| CURRENT_STATE |

## Target Tables (Outputs)
- → [[TMP_SCD2_USER_SERVICES_C_REC]]
| Column Name |
|---|
| USER_ID |
| FIRST_DATE |
| LAST_DATE |
| CURRENT_STATE |
| CURRENT_RECORD |
- → [[TMP_SCD2_USER_SERVICES_P_REC]]
| Column Name |
|---|
| USER_ID |
| FIRST_DATE |
| LAST_DATE |
| CURRENT_STATE |
| CURRENT_RECORD |
- → [[SCD2_USER_SERVICES]]
| Column Name |
|---|
| USER_ID |
| FIRST_DATE |
| LAST_DATE |
| CURRENT_STATE |
| CURRENT_RECORD |

