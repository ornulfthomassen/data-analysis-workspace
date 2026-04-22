# VYA_ADM_HIST_PROD_PRICE_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a historical monthly dimension of product pricing information. It joins monthly periods with historical product attributes to show the monthly fee (price) for products that were active during each month. The data is filtered for 'Telenor' brand, 'Abonnement' (Subscription) product category, and 'Consumerprodukt' (Consumer product) reporting, including data up to the end of the current year.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_PRODUCT_ATTRIBUTE_HIST]]

