# ORDER_LINE_DETAIL_MOB_V

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates and enriches detailed mobile order line transaction data with comprehensive dimensional information (dates, products, customers, dealers, service providers) and calculates various sales and churn-related Key Performance Indicators (KPIs). It provides a consolidated dataset for in-depth analytical reporting on mobile business performance, including tracking of specific product features, campaign activities, and regret orders, focusing on current and recent historical data within specific business and market areas.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_MOB_FACT_V]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.BINDING_TYPE_BENEFIT_DIM]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.CUSTOMER_DIM]]
- ← [[GALAXY.SUBSCR_USER_LOC_DIM_V]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[GALAXY.ORDER_CATEGORY_DIM]]
- ← [[CCDW.SERVICE_PROVIDER]]
- ← [[GALAXY.ORDER_STATUS_DIM_MV]]
- ← [[GALAXY.SEGMENT_DIM_V]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_EXT]]
- ← [[CCDW.SUBSCRIBED_PRODUCT]]

