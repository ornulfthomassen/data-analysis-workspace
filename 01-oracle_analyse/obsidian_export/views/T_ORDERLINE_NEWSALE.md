# T_ORDERLINE_NEWSALE

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies and ranks new sales order lines for specific consumer products (specifically 'Abonnement', 'Tale', and 'Frihet' product family) that meet certain criteria, such as positive KPI for new sales, recent order dates (after 2016), and specific order line types (1 or 2). It joins sales fact data with product, order line type, and dealer dimensions to provide details like dealer name and sales channel descriptions, while excluding sales from a predefined list of dealers.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
| Column Name |
|---|
| ORDERLINE_PRODUCT_KEY |
| ORDER_LINE_TYPE_KEY |
| DEALER_KEY |
| kpi_newsale |
| order_dt_key |
| resource_value |
- ← [[GALAXY.ORDER_LINE_PRODUCT_DIM_V]]
| Column Name |
|---|
| ORDER_LINE_PRODUCT_KEY |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_REPORTING |
| PRODUCT_FAMILY_NAME |
- ← [[GALAXY.ORDER_LINE_TYPE_DIM]]
| Column Name |
|---|
| ORDERLINE_TYPE_KEY |
- ← [[GALAXY.DEALER_DIM]]
| Column Name |
|---|
| DEALER_KEY |
| DEALER_NAME |
| DRM_SALES_CHANNEL_GEN02_DESC |
| DRM_SALES_CHANNEL_GEN03_DESC |

