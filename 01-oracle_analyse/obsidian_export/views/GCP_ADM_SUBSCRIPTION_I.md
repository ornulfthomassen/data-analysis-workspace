# GCP_ADM_SUBSCRIPTION_I

**Schema:** `CCM` | **Type:** `View`

## Description
This view, 'GCP_ADM_SUBSCRIPTION_I', provides a comprehensive, monthly aggregated snapshot of subscription-related data for analytical purposes, likely for ingestion into a data lake (Mjøsa) or Google Cloud Platform (GCP). It combines detailed information about subscriptions, customer demographics, product offerings, device usage, market areas, porting activities, and extensive historical usage metrics (mobile data, MMS, SMS, voice traffic) and revenue figures (gross/net fees, usage, discounts, adjusted revenue) over the last three months. It also includes specific flags and statuses like 'Next Familie' discount status and 'SWAP' status, and filters out certain internal customer accounts. The view is designed to offer a holistic and timely picture of each subscription's performance and characteristics.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY_I]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
- ← [[CRM_ANALYSE.PD]]
- ← [[CRM_ANALYSE.ADM_MOBIL_SUBSCR_HIST]]
- ← [[CRM_ANALYSE.ADM_SERVICE_PROVIDER_DIM]]
- ← [[CRM_ANALYSE.ADM_MARKET_AREA_DIM]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_AGG_I]]
- ← [[CLM_ADM.ADM_SUBSCR_HANDSET_HIST_I]]
- ← [[CLM_ADM.ADM_GSMA_MARKETING_NAME_DIM]]
- ← [[CLM_ADM.ADM_MOB_SUBS_REVENUE_3MO]]
- ← [[CLM_ADM.ADM_PROFIT_CAT_SUBS_HIST]]
- ← [[CRM_ANALYSE.ADM_PROFIT_CAT_DIM]]
- ← [[CLM_ADM.ADM_PROFIT_CAT_MND_SUBS_HIST]]
- ← [[CLM_ADM.ADM_MOBIL_PORT_HISTORY]]
- ← [[CLM_ADM.ADM_DEVICE_AGREEMENT]]
- ← [[CLM_ADM.ADM_CUST_NEXT_FAMILIE_AGG]]
- ← [[CLM_ADM.ADM_SUBS_NEXT_FAMILIE_AGG]]

