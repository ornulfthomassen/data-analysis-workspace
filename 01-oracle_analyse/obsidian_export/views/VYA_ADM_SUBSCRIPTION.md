# VYA_ADM_SUBSCRIPTION

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive, monthly snapshot of subscription data, intended for loading into a data warehouse (referred to as 'Mjøsa' in the comments). It aggregates various historical and current details related to each subscription, including customer information, product attributes, device usage, traffic statistics (data, MMS, SMS, voice), revenue figures, and status for programs like 'Next Familie Rabatt' and 'SWAP' agreements. The data is time-bound by 'PERIOD_MONTH_KEY', indicating a historical perspective on subscription attributes and activities.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
- ← [[CLM_ADM.ADM_SUBSCR_DETAIL_HIST]]
- ← [[CRM_ANALYSE.PD]]
- ← [[CLM_ADM.ADM_PRODUCT_ATTRIBUTE_HIST]]
- ← [[CRM_ANALYSE.ADM_MOBIL_SUBSCR_HIST]]
- ← [[CRM_ANALYSE.ADM_SERVICE_PROVIDER_DIM]]
- ← [[CRM_ANALYSE.ADM_MARKET_AREA_DIM]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_AGG]]
- ← [[CLM_ADM.ADM_SUBSCR_HANDSET_HIST]]
- ← [[CLM_ADM.ADM_GSMA_MARKETING_NAME_DIM]]
- ← [[CLM_ADM.ADM_MOB_SUBS_REVENUE_3MO]]
- ← [[CLM_ADM.ADM_PROFIT_CAT_SUBS_HIST]]
- ← [[CRM_ANALYSE.ADM_PROFIT_CAT_DIM]]
- ← [[CLM_ADM.ADM_PROFIT_CAT_MND_SUBS_HIST]]
- ← [[CLM_ADM.ADM_MOBIL_PORT_HISTORY]]
- ← [[CLM_ADM.ADM_DEVICE_AGREEMENT]]
- ← [[CLM_ADM.ADM_CUST_NEXT_FAMILIE_AGG]]
- ← [[CLM_ADM.ADM_SUBS_NEXT_FAMILIE_AGG]]

