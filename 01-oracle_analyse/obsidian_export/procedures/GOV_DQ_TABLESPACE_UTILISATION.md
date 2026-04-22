# GOV_DQ_TABLESPACE_UTILISATION

**Schema:** `CCM` | **Type:** `Procedure`

## Description
The procedure monitors and reports on Oracle tablespace utilization. It first calculates detailed usage statistics (allocated, free, used space, auto-extensible max size, etc.) for both permanent and temporary tablespaces, storing these metrics in the `CLM_CCM.CLM_TABLESPACE` table. Subsequently, it uses these metrics to generate data quality (DQ) assessment records, classifying tablespace status (OK, WARNING, ERROR) based on free space percentages, and inserts these assessments into the `CLM_CCM.GOV_DQ_MARTS` table. The `CLM_CCM.CLM_TABLESPACE` table is dropped and re-created on each execution to ensure fresh data.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
- ← [[DBA_DATA_FILES]]
- ← [[DBA_LMT_FREE_SPACE]]
- ← [[SYS.TS$]]
- ← [[SYS.V_$TEMP_SPACE_HEADER]]
- ← [[DBA_TEMP_FILES]]
- ← [[SYS.V_$TEMP_EXTENT_POOL]]
- ← [[SYS.DBA_TABLESPACES]]
- ← [[CLM_CCM.CLM_TABLESPACE]]
- ← [[CLM_CCM.GOV_DQ_MARTS]]

## Target Tables (Outputs)
- → [[CLM_CCM.CLM_TABLESPACE]]
- → [[CLM_CCM.GOV_DQ_MARTS]]

