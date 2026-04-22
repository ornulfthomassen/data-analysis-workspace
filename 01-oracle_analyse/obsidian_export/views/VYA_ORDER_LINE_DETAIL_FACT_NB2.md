# VYA_ORDER_LINE_DETAIL_FACT_NB2

**Schema:** `CCM` | **Type:** `View`

## Description
This Oracle SQL view, `VYA_ORDER_LINE_DETAIL_FACT_NB2`, is designed to construct detailed order line fact records. Its primary purpose is to capture and standardize information related to 'Nettbutikken' (webshop) initiated device changes or new device sales that might not originate from traditional order entries. It populates a wide range of fact and dimension attributes, often using fixed values (e.g., for order category, KPIs like `KPI_NEWSALE` and `KPI_GROSS_SALE_CE`, indicating specific types of transactions). The view integrates device insight data with various related dimension tables (date, dealer, device) and specifically filters out records that are already present in the main `ORDER_LINE_DETAIL_FACT_MV` by checking for `NULL` IMEI values from that materialized view, suggesting it acts as a supplementary source for specific webshop transactions.

## Data Sources (Inputs)
- ← [[CCM.VYA_INSIGHT_DEVICE_FROM_NB]]
- ← [[GALAXY.DEVICE_DIM]]
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.DEALER_DIM]]

