# ADM03_ADDR_COVERAGE_HIST

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Creates and maintains the `CRM_ANALYSE.ADM_ADDR_COVERAGE_HIST` partitioned table. It checks for the table's existence and creates it if missing, including initial partitioning and unique indexing on `FARID, PERIOD_MONTH_KEY`. Subsequently, it identifies the latest processed month in the historical table and, if a newer month's data (specifically, the previous calendar month) is available and not yet processed, it adds a new partition (if needed) and inserts detailed address coverage information from `CLM_CCM.CCM_COVERAGE_NEW` into the historical table for that month. It also logs processing events using `CRM_ANALYSE.P_ADM_LOAD_HISTORY`.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
- ← [[DUAL]]
- ← [[CRM_ANALYSE.ADM_ADDR_COVERAGE_HIST]]
- ← [[CLM_CCM.CCM_COVERAGE_NEW]]

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_ADDR_COVERAGE_HIST]]

