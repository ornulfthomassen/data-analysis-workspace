# VYAMN_ORDER_LINE_DETAIL_FACT

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `VYAMN_ORDER_LINE_DETAIL_FACT`, serves as a comprehensive fact table for mobile order line details, designed for analytical reporting (likely for a data warehouse named 'MJØSA'). It enriches raw order line data with extensive dimensional attributes and Key Performance Indicators (KPIs). The view joins multiple dimension tables to provide detailed information about orders, products, subscriptions, customers (owner and user), geographical locations, dates, and various sales-related metrics. Key functionalities include: data type casting, derivation of descriptive fields (e.g., order category, termination reason), calculation of customer ages, population of device information (IMEI, handset SK), and computation of numerous KPIs related to sales, churn, product changes, and specific service types (e.g., speech, MBB, FWA). It consolidates order-related data for in-depth analysis of mobile service transactions.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_MOB_FACT_MV]]
- ← [[GALAXY.ORDER_TIME_DIM_V]]
- ← [[GALAXY.ORDER_CATEGORY_DIM]]
- ← [[GALAXY.ADD_ON_MOB_ORDER_CATEGORY_DIM]]
- ← [[GALAXY.TERMINATION_REASON_DIM_V]]
- ← [[CLM_ADM.ADM_PRODUCT_ATTRIBUTE_HIST]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.SUBSCR_USER_LOC_DIM_V]]
- ← [[GALAXY.CUSTOMER_DIM_MV]]
- ← [[GALAXY.DEVICE_DIM]]
- ← [[CCM.MO]]
- ← [[CCM.MU]]
- ← [[CCM.ASM]]
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
- ← [[CCM.HWO_IMEI]]

