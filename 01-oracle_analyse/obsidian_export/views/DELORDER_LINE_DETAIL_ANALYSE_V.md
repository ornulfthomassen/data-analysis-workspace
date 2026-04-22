# DELORDER_LINE_DETAIL_ANALYSE_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, named "DELORDER_LINE_DETAIL_ANALYSE_V", serves as a comprehensive analytical dataset for mobile order line transactions. It combines detailed order information with product attributes, binding details, dealer and sales channel data, campaign insights, and customer demographics. Its primary purpose is to enable in-depth analysis of sales performance, including new sales, terminations, porting activities, product changes (upsale, downsale, neutral, crossbrand), and the impact of marketing campaigns. The view enriches raw transaction data with various derived metrics, geographical information, and customer segmentation attributes, specifically filtered for the 'MOBILE' business area and relevant order statuses.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.BINDING_TYPE_BENEFIT_DIM]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[CRM_ANALYSE.DIMPOSTNUMMER_T]]
- ← [[CRM_ANALYSE.DIMPOSTNUMMER]]
- ← [[GALAXY.BUSINESS_AREA_DIM_V]]
- ← [[GALAXY.ORDER_LINE_TYPE_DIM]]
- ← [[GALAXY.MARKET_AREA_DIM]]
- ← [[GALAXY.ORDER_STATUS_DIM_MV]]
- ← [[GALAXY.HANDSET_DIM_V]]
- ← [[GALAXY.FROM_ORDER_PRODUCT_DIM_V]]
- ← [[CCM.CCM_CUSTOMER]]
- ← [[CRM_ANALYSE.HOUSEHOLD_LAT_LONG_SHOP_V]]
- ← [[GALAXY.BINDING_PRODUCT_DIM_V]]
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]
- ← [[CRM_ANALYSE.KIM_CHANNEL_DIM]]
- ← [[GALAXY.CAMPAIGN_HIT_TYPE_DIM]]
- ← [[CRM_ANALYSE.BR_ANALYTIC_UNIVERSE_SUBSET]]
- ← [[CRM_ANALYSE.NRPORT_SERVICE_PROVIDER]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CRM_ANALYSE.ADM_QUAL_OFFER_HIST_SUBSCR]]

