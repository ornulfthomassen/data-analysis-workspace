# ORDER_LINE_DETAIL_FACT_BUS_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, named 'ORDER_LINE_DETAIL_FACT_BUS_V', serves as a comprehensive fact table for detailed order line analysis in a business intelligence or data warehousing context. It consolidates and enriches core order line data with related information from customer mappings, subscription master data, and time dimensions. Specifically, it joins order line details with customer ownership and usage, subscription information, and converts date and time keys into readable datetime formats (OSD_DTTM, OD_DTTM). It calculates and presents a wide array of attributes including various keys, indicators (KPIs for sales, porting, churn, etc.), product details, campaign references, and resource values, making it suitable for granular reporting and analytical queries related to order line performance, customer behavior, and operational metrics.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_MOB_BUS_MV]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[GALAXY.ORDER_TIME_DIM_V]]

