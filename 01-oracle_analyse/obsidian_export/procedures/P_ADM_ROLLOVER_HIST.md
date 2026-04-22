# P_ADM_ROLLOVER_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The `P_ADM_ROLLOVER_HIST` procedure processes and loads historical rollover unit data for a given month (`P_YYYYMM`). It performs a multi-stage ETL (Extract, Transform, Load) process:
1.  **Raw Data Loading**: It first extracts raw rollover unit data from `OCS.OCS_FREE_UNITS` and `CLM_ADM.ADM_MONTH_DIM` (with specific exclusions) into a temporary table (`TMP_ROLLOVER_HIST_RAW`), which is then exchanged into a partition of the permanent `ADM_ROLLOVER_HIST_RAW` table.
2.  **Historical Data Transformation**: It then transforms this raw data by joining it with other dimension tables (`PCAT.COMPONENT`, `CCDW.SUBSCRIPTION_MAPPING`, `CM.SUBSCRIPTION_OFFER_INCENTIVE`) and performing calculations. The results are loaded into another temporary table (`TMP_ROLLOVER_HIST`), which is then exchanged into a partition of the permanent `ADM_ROLLOVER_HIST` table.
3.  **Monthly Summary Generation**: If the processing month is the previous month, it calculates and stores aggregated rollover balances for the current, previous, and two months prior (three months in total) into a permanent summary table named `ADM_ROLLOVER_LAST`. This involves dropping and recreating the `ADM_ROLLOVER_LAST` table.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[OCS.OCS_FREE_UNITS]]
- ← [[CLM_ADM.ADM_ROLLOVER_HIST_RAW]]
- ← [[PCAT.COMPONENT]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[CM.SUBSCRIPTION_OFFER_INCENTIVE]]
- ← [[CLM_ADM.ROLLOVER_%]]
- ← [[CLM_ADM.ADM_ROLLOVER_HIST]]

## Target Tables (Outputs)
- → [[ADM_ROLLOVER_HIST_RAW]]
- → [[TMP_ROLLOVER_HIST_RAW]]
- → [[ADM_ROLLOVER_HIST]]
- → [[TMP_ROLLOVER_HIST]]
- → [[ADM_ROLLOVER_LAST]]

