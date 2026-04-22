# V_ANALYTICAL_MASTER_TABLE_MBB

**Schema:** `CCM` | **Type:** `View`

## Description
This view, 'V_ANALYTICAL_MASTER_TABLE_MBB', is designed to create a comprehensive analytical master table for Mobile Broadband (MBB) subscriptions. It aggregates historical data on subscriptions, customer information, product details, device usage, and traffic data (data, MMS, SMS, voice calls) from various sources for specific monthly periods. It also includes revenue metrics. The view links different historical snapshots to provide a holistic view of each subscription and its associated entities over time, facilitating detailed analysis of MBB customer behavior, product adoption, device characteristics, and revenue performance.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
- ← [[CLM_ADM.ADM_SUBSCR_DETAIL_HIST]]
- ← [[CLM_ADM.ADM_MBB_SUBSCR_DETAIL_HIST]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_AGG]]
- ← [[CLM_ADM.ADM_SUBSCR_HANDSET_HIST]]
- ← [[CLM_ADM.ADM_GSMA_MARKETING_NAME_DIM]]

