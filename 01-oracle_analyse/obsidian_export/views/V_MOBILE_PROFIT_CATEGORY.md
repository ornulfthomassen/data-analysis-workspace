# V_MOBILE_PROFIT_CATEGORY

**Schema:** `CCM` | **Type:** `View`

## Description
This view links subscription information with category-specific data, providing the subscription ID, a reporting period key, a derived 'profit period' key (two months prior to the reporting period), and a category. It effectively prepares data for category-based profit analysis or reporting at a subscription level, possibly incorporating a time lag for profit calculation.

## Data Sources (Inputs)
- ← [[PROFIT.CP_CAT_BED_PRIV]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]

