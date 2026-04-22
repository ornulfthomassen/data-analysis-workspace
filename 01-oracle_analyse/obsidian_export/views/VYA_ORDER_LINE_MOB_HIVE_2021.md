# VYA_ORDER_LINE_MOB_HIVE_2021

**Schema:** `CCM` | **Type:** `View`

## Description
This view, named VYA_ORDER_LINE_MOB_HIVE_2021, serves as a comprehensive analytical dataset for mobile order line details, specifically for data with an order status date before 2022. It enriches core transactional order line data by integrating information from various dimension tables, such as order time, categories, termination reasons, dates, customer demographics, and geographical details. The view calculates numerous Key Performance Indicators (KPIs) related to sales, porting, product changes, terminations, and device swaps, as well as descriptive fields for regret orders and customer age groups. It casts and converts several keys into more readable or specific date/time formats and extracts geographical information (postal code, municipality, county) from customer data. The view is designed for analytical consumption, potentially by platforms like SAS Viya, and hints at being a year-specific snapshot or partition of a larger order line fact table.

## Data Sources (Inputs)
- ← [[CCM.ORDER_LINE_MOB_HIVE_2021]]
- ← [[GALAXY.ORDER_TIME_DIM_V]]
- ← [[GALAXY.ORDER_CATEGORY_DIM]]
- ← [[GALAXY.TERMINATION_REASON_DIM_V]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
- ← [[CCM.ASM_2021]]
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
- ← [[CLM_ADM.MUNICIPALITY_COUNTY_REGION_DIM]]

