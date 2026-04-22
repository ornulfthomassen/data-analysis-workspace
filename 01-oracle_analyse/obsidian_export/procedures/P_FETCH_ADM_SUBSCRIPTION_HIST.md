# P_FETCH_ADM_SUBSCRIPTION_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure iterates through monthly periods from July 2022 to August 2024. For each period, it dynamically creates a new permanent table named 'CLM_ADM.ADM_SUBSCRIPTION_YYYYMM' (where YYYYMM is the period key). It populates these tables by selecting distinct subscription history records from the source table 'CCM.VYA_ADM_SUBSCRIPTION', filtered by the current monthly period. For periods from January 2023 onwards, it explicitly drops the target table if it exists before recreating it. Logging is performed for table creation and row counts, with error handling for empty or uncreated tables.

## Data Sources (Inputs)
- ← [[CCM.VYA_ADM_SUBSCRIPTION]]
- ← [[SYS.ALL_OBJECTS]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_SUBSCRIPTION_YYYYMM]]

