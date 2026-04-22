# ADM10_SUBSCRIPTION_HISTORY_I

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Processes monthly mobile subscription history data. It extracts subscription data for a given month (`V_YYYYMM`), filters out records already present in the `ADM_SUBSCRIPTION_HISTORY` table, and then identifies the latest (maximum `SUBSCRIPTION_KEY_NEXT`) subscription record per `MAIN_NUMBER`. This refined data is then loaded into a dedicated partition of the permanent `ADM_SUBSCRIPTION_HISTORY_I` table using an `EXCHANGE PARTITION` operation.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM]]
- ← [[CRM_ANALYSE.TDM_MOBIL_SUBSCR_HIST]]
- ← [[ADM_SUBSCRIPTION_HISTORY]]

## Target Tables (Outputs)
- → [[TMP_SUBSCRIPTION_HISTORY_I1]]
- → [[TMP_SUBSCRIPTION_HISTORY_I1B]]
- → [[TMP_SUBSCRIPTION_HISTORY_I2]]
- → [[ADM_SUBSCRIPTION_HISTORY_I]]

