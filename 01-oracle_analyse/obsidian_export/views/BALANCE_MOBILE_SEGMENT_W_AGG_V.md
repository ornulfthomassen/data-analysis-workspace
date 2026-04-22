# BALANCE_MOBILE_SEGMENT_W_AGG_V

**Schema:** `CCM` | **Type:** `View`

## Description
Consolidates and standardizes aggregated mobile segment balance data from different internal sources, including net balance adjustments (subtracting 'OUT_PORT') for customer subscriptions. It enriches this data with product information, assigns various segmentation and product category details (defaulting to 'Ukjent'/'Unknown' when not available), and aggregates data on a weekly and monthly basis. The view filters out specific product descriptions (e.g., 'BEDRIFT', 'DEMO', 'TVILLING', 'FASTNETT') and combines general mobile segment balances with specific Talkmore balance data.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.BALANCE_MOBILE_SEGMENT_W_AGG]]
- ← [[CLM_ADM.BALANCE_TALKMORE_WEEK_AGG]]
- ← [[GALAXY.PRODUCT_DIM]]

