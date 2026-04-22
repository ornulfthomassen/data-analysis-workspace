# VYA_ORDER_LINE_MOB_HIVE_2018

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive, denormalized dataset of mobile order line details, primarily focusing on order status dates before 2019 (suggesting data for the year 2018 and prior). It enriches core order line information with various attributes and Key Performance Indicators (KPIs) related to sales, subscriptions, customer demographics (age, location), product categories, termination reasons, agreement details, and swap activities. The view is designed to facilitate detailed analytical reporting and insights into mobile order trends and performance.

## Data Sources (Inputs)
- ← [[CCM.ORDER_LINE_MOB_HIVE_2018]]
- ← [[GALAXY.ORDER_TIME_DIM_V]]
- ← [[GALAXY.ORDER_CATEGORY_DIM]]
- ← [[GALAXY.TERMINATION_REASON_DIM_V]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
- ← [[CCM.ASM_2018]]
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
- ← [[CLM_ADM.MUNICIPALITY_COUNTY_REGION_DIM]]

