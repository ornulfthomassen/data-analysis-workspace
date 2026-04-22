# GCP_ADM_SUBSCRIPTION_CURRENT

**Schema:** `CCM` | **Type:** `View`

## Description
This view, named "GCP_ADM_SUBSCRIPTION_CURRENT", provides a comprehensive, multi-dimensional monthly snapshot of current active mobile subscriptions. It aggregates extensive details including customer information (owner, user), subscription lifecycle events (start dates, reasons, change types, porting activities), product attributes (brand, name, category, profit segmentation), device details (model, OS, manufacturer, type, usage duration), sales channel and dealer information, and a wide array of usage statistics (data, MMS, SMS, voice counts and minutes for domestic and international usage over the last three months, including sums and averages). Additionally, it incorporates various revenue figures (gross, net, periodic, other fees, discounts) and status indicators for specific programs like 'Next Familie Rabatt' and 'SWAP agreements'. The view aims to offer a holistic, analytical perspective of active subscriptions, primarily reflecting data for the most recently completed month based on `SYSDATE-1` logic.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CCDW.SUBSCRIPTION_HANDSET]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]
- ← [[CLM_ADM.ADM_SUBS_USAGE_MOB_MONTH_AGG]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CRM_ANALYSE.ADM_LAST_PERIOD]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[CRM_ANALYSE.PD]]
- ← [[CLM_ADM.ADM_PRODUCT_ATTRIBUTE_HIST]]
- ← [[CRM_ANALYSE.ADM_MOBIL_SUBSCR_HIST]]
- ← [[CRM_ANALYSE.ADM_SERVICE_PROVIDER_DIM]]
- ← [[CRM_ANALYSE.ADM_MARKET_AREA_DIM]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_AGG]]
- ← [[CLM_CCM.CCM_SUBS_EQUIPMENT_INFO_V]]
- ← [[GALAXY.HANDSET_DIM_V]]
- ← [[CLM_ADM.ADM_MOB_SUBS_REVENUE_3MO]]
- ← [[CLM_ADM.ADM_PROFIT_CAT_SUBS_HIST]]
- ← [[CRM_ANALYSE.ADM_PROFIT_CAT_DIM]]
- ← [[CLM_ADM.ADM_PROFIT_CAT_MND_SUBS_HIST]]
- ← [[CLM_ADM.ADM_MOBIL_PORT_HISTORY]]
- ← [[CLM_ADM.ADM_DEVICE_AGREEMENT]]
- ← [[CLM_ADM.ADM_CUST_NEXT_FAMILIE_AGG]]
- ← [[CLM_ADM.ADM_SUBS_NEXT_FAMILIE_AGG]]

