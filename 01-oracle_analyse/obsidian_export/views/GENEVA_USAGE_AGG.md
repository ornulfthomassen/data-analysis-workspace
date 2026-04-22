# GENEVA_USAGE_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates monthly subscription usage data, including various metrics like net and gross usage amounts, discount amounts, call start price, total volume, number of events, and duration. It categorizes and enriches this usage data using information from product dimensions, CPA business models, and traffic type dimensions. The aggregated data is grouped by several granular dimensions such as period month, subscription, product, market area, agreement, discount type, call type, traffic report groups, handset, roaming and destination countries, twin switch, APN, and content provider. It also counts the number of unique 'twin' subscriptions (SUB_NUMBER). The main purpose is to prepare usage data for loading into another system, potentially 'MJØSA'.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_USAGE_MONTH_FACT_V]]
- ← [[GALAXY.CPA_BUSINESS_MODEL_DIM_V]]
- ← [[CRM_ANALYSE.PRODUCT_DIM_V]]
- ← [[GALAXY.TRAFFIC_TYPE_DIM_V]]

