# STOCK_MOBILE_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `STOCK_MOBILE_HIST` processes mobile subscription data for a given date to create detailed and aggregated historical snapshots. It first extracts core subscription and product information, then enriches this data with customer demographics, discount details, family bonus flags, and various segmentation attributes (e.g., lifecycle, VAR, churn, profit categories). Finally, it aggregates this enriched data and combines it with pre-existing aggregated Talkmore data to form a comprehensive historical summary, likely for analytical reporting.

## Data Sources (Inputs)
- ← [[GALAXY.PRIMARY_PRODUCT_DIM_V]]
- ← [[CM.SUBSCRIPTION_OFFER_INCENTIVE]]
- ← [[CM.SUBSCRIPTION]]
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
- ← [[PCAT.V_PRODUCT_OFFER_CONFIG_MV]]
- ← [[PCAT.PRODUCT_OFFER]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[CLM_ADM.ADM_PROFIT_CAT_SUBS_HIST]]
- ← [[CRM_ANALYSE.MAP2_SEGMENT_HIST]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.CUSTOMER_DIM]]
- ← [[CRM_ANALYSE.VARSEGMENT_MOBILE]]
- ← [[CRM_ANALYSE.CHURNSEGMENT_MOBILE]]
- ← [[CRM_ANALYSE.LIVSFASESEGMENT_MOBILE]]
- ← [[FINANCE_MART.SUBSCR_PROD_CUST_AGG_TALKMORE]]

## Target Tables (Outputs)
- → [[TMP_STOCK_MOBILE_HIST_CM]]
- → [[TMP_STOCK_MOBILE_HIST_RAW]]
- → [[STOCK_MOBILE_HIST_DET]]
- → [[STOCK_MOBILE_HIST_AGG]]

