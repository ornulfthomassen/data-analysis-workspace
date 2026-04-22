# PP_GCP_TMP_MOBILE_ORDER_LINE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Creates or recreates a temporary staging table named `CLM_ADM.TMP_MOBILE_ORDER_LINE`. This procedure denormalizes detailed mobile order line data from the `GCP_ORDER_LINE_DETAIL_FACT` table by performing multiple joins with various dimension tables (e.g., date, product, dealer, service provider, order status, equipment, sales matrix). The data is filtered based on a provided `PERIOD_MONTH_KEY` and `ORDER_SOURCE`. The resulting table contains a comprehensive, flattened dataset of mobile order line details and associated KPIs, intended for further analysis or reporting.

## Data Sources (Inputs)
- ← [[GCP_ORDER_LINE_DETAIL_FACT]]
- ← [[CLM_ADM.TMP_PRODUCT_DIM]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[GALAXY.ORDER_CATEGORY_DIM]]
- ← [[CCM.VYA_SERVICE_PROVIDER_DIM]]
- ← [[GALAXY.ORDER_LINE_TYPE_DIM]]
- ← [[GALAXY.ORDER_STATUS_DIM_MV]]
- ← [[GALAXY.ORDER_STATUS_REASON_DIM_V]]
- ← [[CLM_ADM.TMP_MOB_EQUIPMENT_DIM]]
- ← [[GALAXY.SALES_MATRIX_DIM]]

## Target Tables (Outputs)
- → [[CLM_ADM.TMP_MOBILE_ORDER_LINE]]

