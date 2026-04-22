# VYA_CCM_PROD_SUBSCR

**Schema:** `CCM` | **Type:** `View`

## Description
Prepares and consolidates product subscription data by grouping unique subscription details (ID, product, business area, load datetime, source system ID) and deriving the earliest valid start date (not before 1970-01-01) and the latest end date. The view is explicitly used for 'LOADING CCM_PRODUCT_SUBSCRIPTION-DATA TO MJØSA', indicating its role in data integration or warehousing.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_PRODUCT_SUBSCRIPTION_V]]

