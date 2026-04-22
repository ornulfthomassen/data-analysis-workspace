# STOCK_MOBILE_HISTORY

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure generates a daily historical snapshot of mobile subscription data. It first extracts raw subscription and product details from operational (CM) and data warehouse (CCDW, GALAXY) sources, then enriches this data with customer demographics, lifecycle segments, profit categories, and calculates various discounts. Finally, it aggregates this comprehensive data, including Talkmore subscriptions, into detailed and aggregated history tables for reporting and analysis.

## Data Sources (Inputs)
- ← [[GALAXY.PRIMARY_PRODUCT_DIM_V]]
- ← [[CM.SUBSCRIPTION_OFFER_INCENTIVE]]
- ← [[CM.SUBSCRIPTION]]
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]
- ← [[CLM_ADM.ADM_PROFIT_CAT_SUBS_HIST]]
- ← [[CRM_ANALYSE.LIVSFASESEGMENT_MOBILE]]
- ← [[CLM_ADM.ADM_PRODUCT_ATTRIBUTE_HIST]]
- ← [[CLM_ADM.ADM_DISCOUNT_PRODUCT_DIM]]
- ← [[GALAXY.TALKMORE_SUBSCRIPTION_AGG]]

## Target Tables (Outputs)
- → [[TMP_STOCK_MOBILE_HISTORY_CM]]
- → [[TMP_STOCK_MOBILE_HISTORY_RAW]]
- → [[STOCK_MOBILE_HISTORY_DET]]
- → [[TMP_STOCK_MOBILE_HISTORY_AGG_SUB]]
- → [[STOCK_MOBILE_HISTORY_AGG]]

