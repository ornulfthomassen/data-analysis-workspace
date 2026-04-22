# VYA_ORDER_LINE_DETAIL_FACT_FT

**Schema:** `CCM` | **Type:** `View`

## Description
This view extracts detailed order line information primarily focused on terminated fixed-term device insurance agreements. It populates a fact table with various order-line specific attributes and Key Performance Indicators (KPIs), specifically marking 'KPI_TERMINATION' as 1. The data seems to be used for analytical purposes related to hardware orders and device insurance in the Telenor online store (Nettbutikken telenor.no). It filters for agreements with a root product ID of '770' and specific end-date intervals (24 or 60 months from the original start date), and for products categorized as 'Avtaleprodukt', 'DEVICE', 'Forsikring', and 'Consumerprodukt'.

## Data Sources (Inputs)
- ← [[ODS.AGREEMENT_ODS_MOB]]
- ← [[ODS.AGREEMENT_OFFER_ODS_MOB]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.CUSTOMER_DIM]]
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
- ← [[GALAXY.SUBSCR_OWNER_LOC_DIM_V]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[CCDW_ORDER.ORDER_MAPPING]]

