# VYA_ORDER_LINE_MOB_HIVE_2019

**Schema:** `CCM` | **Type:** `View`

## Description
This view, named `VYA_ORDER_LINE_MOB_HIVE_2019`, provides a comprehensive, enriched dataset of mobile order line items. It integrates core order details with extensive information on order categories, termination reasons, customer demographics (owner and user age, age groups, and location data), subscription details, and a wide array of key performance indicators (KPIs) related to sales, churn, product changes, and regretted/canceled orders. The view specifically filters data to include only order lines with an order status date prior to January 1, 2020, suggesting its purpose is for historical reporting and analytical insights into mobile order trends and performance up to the end of 2019.

## Data Sources (Inputs)
- ← [[CCM.ORDER_LINE_MOB_HIVE_2019]]
- ← [[GALAXY.ORDER_TIME_DIM_V]]
- ← [[GALAXY.ORDER_CATEGORY_DIM]]
- ← [[GALAXY.TERMINATION_REASON_DIM_V]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
- ← [[CCM.ASM_2019]]
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
- ← [[CLM_ADM.MUNICIPALITY_COUNTY_REGION_DIM]]

