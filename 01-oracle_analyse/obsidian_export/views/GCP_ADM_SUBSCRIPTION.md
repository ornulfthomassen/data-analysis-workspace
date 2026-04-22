# GCP_ADM_SUBSCRIPTION

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `GCP_ADM_SUBSCRIPTION`, provides a comprehensive monthly snapshot of mobile subscription data primarily for analytical purposes and loading into a data warehouse (referred to as 'Mjøsa' and 'GCP through Denodo integration'). It aggregates detailed information about subscriptions, including customer demographics, product details, device usage (first/last use dates, model, OS, producer), service usage (mobile data, MMS, SMS, voice traffic for domestic and international, including costs, aggregated over the last 3 months), revenue figures (gross/net fees, usage, discounts), sales channel information, porting details (in/out), profit category/segmentation, and specific subscription statuses like 'Next Familie Rabatt' and device swap status. The data is filtered to include active private customers and excludes certain internal or test accounts.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
- ← [[CRM_ANALYSE.PD]]
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

