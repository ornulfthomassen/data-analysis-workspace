# V_CCM_NEXT_FAMILIE_RAPPORTERING

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a multi-level report on 'Next Familie' (Next Family) mobile subscriptions. It aggregates data on 'Next Familie Voksen' (adult), 'Next Familie Under 18' (under 18), and 'full price' family subscriptions. The report is presented at three levels of detail: a grand total for all 'Next' products per month, subtotals per specific 'Next' product per month, and a more granular breakdown per product and discount configuration, showing counts of associated subscriptions.

## Data Sources (Inputs)
- ← [[CLM_ADM.STOCK_MOBILE_HISTORY_MONTH_DET]]
- ← [[GALAXY.PRODUCT_DIM]]

