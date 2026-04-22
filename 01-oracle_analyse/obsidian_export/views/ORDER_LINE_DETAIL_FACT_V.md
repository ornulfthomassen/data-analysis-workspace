# ORDER_LINE_DETAIL_FACT_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `ORDER_LINE_DETAIL_FACT_V`, serves as a comprehensive fact table for detailed mobile order line data. It consolidates a vast array of order-related attributes and key performance indicators (KPIs) by joining the primary order line fact table with various dimension and mapping tables. The view enriches the core order line data with customer, subscription, time, and location details, including mapping customer and subscription IDs. Its purpose is explicitly stated as 'LOADING Order-DATA TO MJØSA', suggesting it's designed to prepare and stage detailed order line information for a data warehouse or analytical data mart ('Mjøsa'). It also derives specific datetime fields from key values.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_MOB_FACT_MV]]
- ← [[GALAXY.ORDER_TIME_DIM_V]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.SUBSCR_USER_LOC_DIM_V]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[GALAXY.ORDER_LINE_DETAIL_MOB_FACT_V]]

