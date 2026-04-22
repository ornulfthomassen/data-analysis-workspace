# ORDER_LINE_DETAIL_FACT_SRG

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates and enriches detailed mobile order line data for analytical and data loading purposes. It combines primary order line facts with associated customer, subscription, time, and location dimensions, and calculates derived date/time attributes. It appears to serve as a comprehensive source for reporting and loading order-related data into a data warehouse or another analytical system (indicated by 'LOADING Order-DATA TO MJØSA').

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[GALAXY.ORDER_LINE_DETAIL_MOB_FACT_V]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[GALAXY.ORDER_LINE_DETAIL_MOB_FACT_SRG]]
- ← [[GALAXY.ORDER_TIME_DIM_V]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.SUBSCR_USER_LOC_DIM_V]]

