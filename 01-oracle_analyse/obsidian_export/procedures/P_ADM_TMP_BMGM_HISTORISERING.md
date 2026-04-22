# P_ADM_TMP_BMGM_HISTORISERING

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure's main functionality is to create daily historical snapshots of two source tables. It dynamically generates two new tables, each named with a date suffix (YYYYMMDD) appended to a base name, by copying all data from the respective source tables. This process effectively 'historizes' the data from the source tables into date-stamped copies.

## Data Sources (Inputs)
- ← [[AGR.BMGM_COUNTS_KURT]]
- ← [[AGR.BMGM_ACCESSES_KURT]]

## Target Tables (Outputs)
- → [[ADM_BMGM_COUNTS_KURT_YYYYMMDD]]
- → [[ADM_BMGM_ACCESSES_KURT_YYYYMMDD]]

