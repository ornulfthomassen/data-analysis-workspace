# VYA_ADM_SUBSCRIPTION_CURRENT

**Schema:** `CCM` | **Type:** `View`

## Description
This Oracle SQL view, `VYA_ADM_SUBSCRIPTION_CURRENT`, provides a comprehensive, current-state snapshot of telecommunication subscriptions. It gathers detailed information from various sources including static subscription details, product attributes, customer segments, device information, sales channels, porting details, and aggregated historical usage (data, MMS, SMS, voice) and revenue data (periodic fees, usage-based revenue) for the current reporting period (calculated as SYSDATE-1 month/day). The view is designed to generate a rich dataset for analytical purposes, likely used for customer relationship management, profitability analysis, and operational reporting, potentially for loading into data marts or analytical platforms (like Viya/Mjøsa) as indicated by its name and internal comments.

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
- ← [[CLM_CCM.CCM_HANDSET_DIM_V]]
- ← [[CLM_ADM.ADM_MOB_SUBS_REVENUE_3MO]]
- ← [[CLM_ADM.ADM_PROFIT_CAT_SUBS_HIST]]
- ← [[CRM_ANALYSE.ADM_PROFIT_CAT_DIM]]
- ← [[CLM_ADM.ADM_PROFIT_CAT_MND_SUBS_HIST]]
- ← [[CLM_ADM.ADM_MOBIL_PORT_HISTORY]]
- ← [[CLM_ADM.ADM_DEVICE_AGREEMENT]]
- ← [[CLM_ADM.ADM_CUST_NEXT_FAMILIE_AGG]]
- ← [[CLM_ADM.ADM_SUBS_NEXT_FAMILIE_AGG]]

