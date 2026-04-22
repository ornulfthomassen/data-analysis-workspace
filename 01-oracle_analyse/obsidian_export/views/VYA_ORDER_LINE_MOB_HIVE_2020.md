# VYA_ORDER_LINE_MOB_HIVE_2020

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates and enriches detailed mobile order line data for the year 2020. It combines core order line attributes with descriptive information from various dimension tables, including order categories, termination reasons, dates, customer demographics (age, location), and subscription details. The view calculates and exposes a wide range of Key Performance Indicators (KPIs) related to sales (newsale, gross sale), churn (termination, internal churn), porting, product changes, and device swapping. Its primary purpose is to provide a comprehensive dataset for analytical and reporting needs within a data warehousing environment (indicated by 'Hive' in the name and the structure).

## Data Sources (Inputs)
- ← [[CCM.ORDER_LINE_MOB_HIVE_2020]]
- ← [[GALAXY.ORDER_TIME_DIM_V]]
- ← [[GALAXY.ORDER_CATEGORY_DIM]]
- ← [[GALAXY.TERMINATION_REASON_DIM_V]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
- ← [[CCM.ASM_2020]]
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
- ← [[CLM_ADM.MUNICIPALITY_COUNTY_REGION_DIM]]

