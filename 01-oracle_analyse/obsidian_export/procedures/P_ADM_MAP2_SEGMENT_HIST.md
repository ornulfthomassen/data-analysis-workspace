# P_ADM_MAP2_SEGMENT_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure populates a monthly partition of the `ADM_MAP2_SEGMENT_HIST` table. It first performs data quality checks on source tables (`GALAXY.DATE_DIM_MV`, `CRM_ANALYSE.MAP2_SEGMENT_HIST`, `CLM_ADM.ADM_CUSTOMER_MAPPING_CTRL`) for the specified `P_YYYYMM` period. If checks pass, it ensures the target partition exists in `ADM_MAP2_SEGMENT_HIST` (creating it if necessary, or checking overwrite permissions). It then creates a temporary table (`TMP_MAP2_SEGMENT_HIST`) by joining and transforming data from `CRM_ANALYSE.MAP2_SEGMENT_HIST` and `CLM_ADM.ADM_CUSTOMER_MAPPING`. Finally, it exchanges this temporary table as a new partition into `ADM_MAP2_SEGMENT_HIST` and updates table statistics. The procedure also logs its execution status to a history table.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| YEAR_MONTH_NUMBER |
| DAY |
- ← [[CRM_ANALYSE.MAP2_SEGMENT_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CU_KURT_ID_OWNER |
| EM_CLASSIFICATION |
| MAP_SEGMENT |
| RUN_DATE |
| P_MAP_SEGMENT1 |
| P_MAP_SEGMENT6 |
| P_MAP_SEGMENT5 |
| P_MAP_SEGMENT4 |
| P_MAP_SEGMENT3 |
| P_MAP_SEGMENT2 |
| EM_PROBABILITY |
| IND_MAP_SEGMENT6 |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CTRL]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| STATUS |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |
- ← [[ADM_MAP2_SEGMENT_HIST]]

## Target Tables (Outputs)
- → [[ADM_MAP2_SEGMENT_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK |
| MAP2_SEGMENT_ID |
| MAP2_SEGMENT_NAME |
| RUN_DATE |
| P_MAP_SEGMENT1 |
| P_MAP_SEGMENT6 |
| P_MAP_SEGMENT5 |
| P_MAP_SEGMENT4 |
| P_MAP_SEGMENT3 |
| P_MAP_SEGMENT2 |
| EM_PROBABILITY |
| IND_MAP_SEGMENT6 |
- → [[TMP_MAP2_SEGMENT_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK |
| MAP2_SEGMENT_ID |
| MAP2_SEGMENT_NAME |
| RUN_DATE |
| P_MAP_SEGMENT1 |
| P_MAP_SEGMENT6 |
| P_MAP_SEGMENT5 |
| P_MAP_SEGMENT4 |
| P_MAP_SEGMENT3 |
| P_MAP_SEGMENT2 |
| EM_PROBABILITY |
| IND_MAP_SEGMENT6 |
- → [[CRM_ANALYSE.ADM_LOAD_HISTORY]]

