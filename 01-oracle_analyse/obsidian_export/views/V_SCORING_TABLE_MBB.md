# V_SCORING_TABLE_MBB

**Schema:** `CCM` | **Type:** `View`

## Description
This view, named 'V_SCORING_TABLE_MBB' (Mobile Broadband), serves to consolidate a comprehensive set of historical and current data points for Mobile Broadband subscriptions. Its primary purpose appears to be providing a detailed analytical snapshot for a specific past month (the last full month relative to SYSDATE-5). It gathers subscription lifecycle details, product information, associated device specifications, customer data, usage statistics (data, MMS, SMS, voice traffic over the last 3 months), and various revenue/fee components. The extensive array of metrics suggests it's designed for customer scoring, segmentation, or in-depth performance analysis of Mobile Broadband subscribers, enabling insights into customer behavior, product uptake, and financial contributions.

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

