# SE_FEE_V

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates aggregated net fees (including initiation, periodic, discount, and termination fees) on a monthly basis for subscriptions. The data is enriched with primary and sub-product details (names, groups, market products) and subscription main numbers, specifically filtered for 'Mobil Telefoni' (Mobile Telephony) products and market areas 2 and 4.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_FEE_MONTH_FACT_V]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.SUBSCRIPTION_DIM_MV]]

