# P_ADM_TMP_BMGM_HISTORISERING

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure creates daily historical snapshot tables by copying all data from two source tables (`AGR.BMGM_COUNTS_KURT` and `AGR.BMGM_ACCESSES_KURT`). The newly created tables are named by appending the current date (YYYYMMDD) to a base name (e.g., ADM_BMGM_COUNTS_KURTYYYYMMDD).

## Data Sources (Inputs)
- ← [[AGR.BMGM_COUNTS_KURT]]
- ← [[AGR.BMGM_ACCESSES_KURT]]

## Target Tables (Outputs)
- → [[ADM_BMGM_COUNTS_KURT<YYYYMMDD>]]
- → [[ADM_BMGM_ACCESSES_KURT<YYYYMMDD>]]

