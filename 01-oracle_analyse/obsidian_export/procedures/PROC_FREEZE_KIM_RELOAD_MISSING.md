# PROC_FREEZE_KIM_RELOAD_MISSING

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Reloads missing contact data by extracting minimum and maximum source contact IDs from a missing data table, inserting these ranges into a customer history log, and subsequently refreshing three related materialized views to update derived data.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.missing_in_kim]]
| Column Name |
|---|
| SOURCE_CONTACT_ID |

## Target Tables (Outputs)
- → [[CLM_CDM.CI_CUST_HISTORY_LOG]]
| Column Name |
|---|
| SEQ_KEY |
| JOBNAME |
| TO_SEQ_KEY |
- → [[CRM_ANALYSE.KIM_TREATMENT_DELTA_MV]]
- → [[CRM_ANALYSE.KIM_TREATMENT_UDF_EXT_PIVOT_A]]
- → [[CRM_ANALYSE.KIM_TREATMENT_UDF_EXT_PIVOT]]

