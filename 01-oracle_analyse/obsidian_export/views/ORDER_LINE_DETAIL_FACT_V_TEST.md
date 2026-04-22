# ORDER_LINE_DETAIL_FACT_V_TEST

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `ORDER_LINE_DETAIL_FACT_V_TEST`, serves to consolidate and enrich detailed mobile order line facts. It combines core order line information from `GALAXY.ORDER_LINE_DETAIL_MOB_FACT_MV` with related dimension data, including customer mapping (owner and user), subscription master history, order time details, and subscriber user location. The view calculates specific datetime fields (Order Status DTTM, Order DTTM) and provides a comprehensive set of attributes for each order line, suitable for analytical reporting or data warehousing purposes (as indicated by comments like 'LOADING Order-DATA TO MJØSA'). It incorporates specific logic to filter customer and subscription mapping based on their presence in `GALAXY.ORDER_LINE_DETAIL_MOB_FACT_V`.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_MOB_FACT_MV]]
- ← [[GALAXY.ORDER_TIME_DIM_V]]
- ← [[GALAXY.SUBSCR_USER_LOC_DIM_V]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[GALAXY.ORDER_LINE_DETAIL_MOB_FACT_V]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]

