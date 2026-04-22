# VYA_ODS_SUBSCRIPTION_TWIN

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates comprehensive information for active mobile subscriptions, focusing on their associated device details and usage statistics. It integrates data on subscription identification, product type (specifically 'SIM-kort' products), device manufacturer, marketing name, type, and first/last use dates. Furthermore, it includes detailed usage metrics such as net revenue, MMS/SMS/talk counts, and data consumption for the last 30 days, as well as for the previous three calendar months.

## Data Sources (Inputs)
- ← [[ODS.SUBSCRIBED_OFFER_ODS_MOB]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[LIVE.EUREKA_IMEI]]
- ← [[CLM_ADM.ADM_GSMA_MARKETING_NAME_DIM]]
- ← [[GALAXY.HANDSET_DIM_V]]
- ← [[CRM_ANALYSE.ADM_USAGE_MOBILE_TWIN_D30_V]]
- ← [[CRM_ANALYSE.ADM_USAGE_MOBILE_TWIN_MONTH_V]]

