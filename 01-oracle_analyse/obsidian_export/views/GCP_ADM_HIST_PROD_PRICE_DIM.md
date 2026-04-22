# GCP_ADM_HIST_PROD_PRICE_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
This view creates a historical product price dimension. It combines monthly period information with historical product attributes to show the monthly price of specific products over time. It filters for products of 'Telenor' brand, 'Abonnement' category, and 'Consumerprodukt' reporting type, providing their monthly fee, validity period, and associated monthly dates up to the end of the current year. It also generates surrogate keys for periods and products.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_PRODUCT_ATTRIBUTE_HIST]]

