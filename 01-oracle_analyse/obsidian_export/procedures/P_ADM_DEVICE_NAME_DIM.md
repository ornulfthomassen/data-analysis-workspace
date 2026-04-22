# P_ADM_DEVICE_NAME_DIM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The `P_ADM_DEVICE_NAME_DIM` procedure is responsible for maintaining and synchronizing a dimension table, `ADM_GSMA_MARKETING_NAME_DIM`. It performs three main data manipulation tasks:
1.  **Insert New Records**: It inserts new device marketing name entries from the `ADM_HANDSET_DIM_V` view into `ADM_GSMA_MARKETING_NAME_DIM` if they do not already exist based on `TAC_ID` and certain marketing name criteria.
2.  **Populate Original Model ID**: It updates the `ORIGINAL_MODEL_ID` column in `ADM_GSMA_MARKETING_NAME_DIM` for records where it is currently null, setting its value to that of the `MODEL_ID` column.
3.  **Synchronize Model ID**: It updates the `MODEL_ID` column in `ADM_GSMA_MARKETING_NAME_DIM` to reflect the current `MODELID` from `CLM_CCM.CCM_TERMINAL_TAC` for records where the existing `MODEL_ID` differs from the source.
Additionally, the procedure gathers statistics on the target table (`ADM_GSMA_MARKETING_NAME_DIM`) for performance optimization and logs its execution status and any errors using the `CRM_ANALYSE.P_ADM_LOAD_HISTORY` procedure.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_HANDSET_DIM_V]]
- ← [[CLM_CCM.CCM_TERMINAL_TAC]]
- ← [[CLM_ADM.ADM_GSMA_MARKETING_NAME_DIM]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_GSMA_MARKETING_NAME_DIM]]

