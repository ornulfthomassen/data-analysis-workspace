# VYA_ORDER_LINE_DETAIL_FACT

**Schema:** `CCM` | **Type:** `View`

## Description
This view, VYA_ORDER_LINE_DETAIL_FACT, serves as a comprehensive fact table for order line details, specifically for mobile-related orders. Its primary purpose is to consolidate and enrich order line data from various source systems, including transactional order details, product information, customer demographics, and time dimensions. It calculates and categorizes numerous Key Performance Indicators (KPIs) related to sales events (new sales, reopens, product changes, terminations, porting, upsell/downsell, device swaps, etc.), customer ages, and regret order analysis. The view is designed to be loaded into an analytical system (referred to as Mjøsa/Viya) and provides a detailed, aggregated, and flattened perspective of order line activities for reporting and analytical purposes. It standardizes and casts many columns to specific character types, suggesting its use in data integration scenarios.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_MOB_FACT_MV]]
- ← [[GALAXY.ORDER_TIME_DIM_V]]
- ← [[GALAXY.ORDER_CATEGORY_DIM]]
- ← [[GALAXY.ADD_ON_MOB_ORDER_CATEGORY_DIM]]
- ← [[GALAXY.TERMINATION_REASON_DIM_V]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CLM_ADM.ADM_PRODUCT_ATTRIBUTE_HIST]]
- ← [[GALAXY.SUBSCR_USER_LOC_DIM_V]]
- ← [[GALAXY.CUSTOMER_DIM_MV]]
- ← [[GALAXY.DEVICE_DIM]]
- ← [[CCM.MO]]
- ← [[CCM.MU]]
- ← [[CCM.ASM]]
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
- ← [[CCM.HWO_IMEI]]

