# LIGHT_STOCK_MV

**Schema:** `CCM` | **Type:** `View`

## Description
This Oracle SQL view, `LIGHT_STOCK_MV`, serves as a comprehensive analytical data source primarily focused on customer subscriptions. It consolidates a vast array of information from various CRM, product, usage, and demographic data systems into a single record per subscription. The view provides detailed insights into subscription attributes, associated product details, customer demographics and behavior (both owner and user), usage patterns (data, SMS, minutes, rollover), device characteristics, contractual agreements (binding, swap, porting), geographical location, CRM segmentation (e.g., MAP2, CLM lifecycle), and financial metrics (revenue, binding). Its main purpose is to enable in-depth CRM analysis, reporting, and potentially targeted marketing or segmentation efforts by providing a holistic view of each customer subscription and its context.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_SUBSCRIPTION]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_CCM.CCM_CUSTOMER]]
- ← [[CLM_CCM.CCM_CUSTOMER_INFO_2]]
- ← [[CLM_CCM.CCM_PRODUCT_SUBSCRIPTION]]
- ← [[GALAXY.HANDSET_DIM_V]]
- ← [[GALAXY.SUBSCRIPTION_DIM]]
- ← [[CLM_CCM.CCM_SUBS_EQUIPMENT_INFO]]
- ← [[CLM_CCM.CCM_ROLLOVER]]
- ← [[CRM_ANALYSE.HOUSEHOLD_LAT_LONG_SHOP_V]]
- ← [[CRM_ANALYSE.MUNICIPAL_DIM]]
- ← [[CLM_CCM.CCM_TERMINAL_DETAIL]]
- ← [[CLM_ADM.ADM_GSMA_MARKETING_NAME_DIM]]
- ← [[CRM_ANALYSE.ADM_QUAL_OFFER_HIST_SUBSCR]]
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
- ← [[GALAXY.MARKET_AREA_DIM]]
- ← [[CLM_CCM.CCM_AGREEMENT]]
- ← [[CLM_CCM.CCM_AGREEMENT_MEMBER]]
- ← [[ADHOC_BS.MK_1727_RES]]

