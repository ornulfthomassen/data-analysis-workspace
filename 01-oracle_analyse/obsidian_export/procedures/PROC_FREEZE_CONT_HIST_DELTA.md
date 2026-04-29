# PROC_FREEZE_CONT_HIST_DELTA

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Updates `TO_SEQ_KEY` in `CLM_CDM.CI_CUST_HISTORY_LOG` for 'COMPLETED' records, deriving the new value from joined contact keys between `CLM_CDM.CI_CUST_CONTACT_HISTORY_LOG_V` and `CLM_CDM.CI_CUST_CONTACT_HISTORY_SDW`. Subsequently, it refreshes four CRM-related materialized views.

## Data Sources (Inputs)
- ← [[CLM_CDM.CI_CUST_CONTACT_HISTORY_LOG_V]]
| Column Name |
|---|
| CONTACT_KEY |
- ← [[CLM_CDM.CI_CUST_CONTACT_HISTORY_SDW]]
| Column Name |
|---|
| CONTACT_KEY |

## Target Tables (Outputs)
- → [[CLM_CDM.CI_CUST_HISTORY_LOG]]
| Column Name |
|---|
| TO_SEQ_KEY |
- → [[CRM_ANALYSE.KIM_TREATMENT_DELTA_MV]]
- → [[CRM_ANALYSE.CI_TREATMENT_CHAR_UDF_MV]]
- → [[CRM_ANALYSE.KIM_TREATMENT_UDF_EXT_PIVOT_A]]
- → [[CRM_ANALYSE.KIM_TREATMENT_UDF_EXT_PIVOT]]

