# P_GCP_MOBILE_ORDER_LINE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `P_GCP_MOBILE_ORDER_LINE` constructs a comprehensive `GCP_MOBILE_ORDER_LINE` fact table. It first creates two temporary dimension-like tables (`TMP_MOB_EQUIPMENT_DIM` and `TMP_PRODUCT_DIM`) from `CCM.VYA_MOBILE_EQUIPMENT_DIM` and `CCM.VYA_PRODUCT_DIM` respectively. These temporary tables, along with multiple `GCP_ORDER_LINE_MOB_FACT` variants and several `GALAXY` and `CCM` dimension tables/views, are then joined and transformed to create a new `TMP_MOBILE_ORDER_LINE` table. This temporary table is subsequently renamed to `GCP_MOBILE_ORDER_LINE`, effectively replacing the existing permanent table with updated data. The process also involves dropping existing tables, creating unique indexes, and gathering statistics.

## Data Sources (Inputs)
- ← [[CCM.VYA_MOBILE_EQUIPMENT_DIM]]
- ← [[CCM.VYA_PRODUCT_DIM]]
- ← [[CLM_ADM.GCP_ORDER_LINE_MOB_FACT]]
- ← [[CLM_ADM.GCP_ORDER_LINE_MOB_FACT_FT]]
- ← [[CLM_ADM.GCP_ORDER_LINE_MOB_FACT_HW]]
- ← [[CLM_ADM.GCP_ORDER_LINE_MOB_FACT_NB]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[GALAXY.ORDER_CATEGORY_DIM]]
- ← [[CCM.VYA_SERVICE_PROVIDER_DIM]]
- ← [[GALAXY.ORDER_LINE_TYPE_DIM]]
- ← [[GALAXY.ORDER_STATUS_DIM_MV]]
- ← [[GALAXY.ORDER_STATUS_REASON_DIM_V]]
- ← [[GALAXY.SALES_MATRIX_DIM]]
- ← [[CLM_ADM.TMP_MOB_EQUIPMENT_DIM]]
- ← [[CLM_ADM.TMP_PRODUCT_DIM]]

## Target Tables (Outputs)
- → [[CLM_ADM.TMP_MOB_EQUIPMENT_DIM]]
- → [[CLM_ADM.TMP_PRODUCT_DIM]]
- → [[CLM_ADM.TMP_MOBILE_ORDER_LINE]]
- → [[CLM_ADM.GCP_MOBILE_ORDER_LINE]]

