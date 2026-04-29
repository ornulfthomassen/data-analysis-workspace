# TMP_THEA_FORSIKRING

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates agreement product quantities (opening balance, closing balance, new contracts/customers) by period month, agreement offer, product name, and market area, specifically for insurance-related products, filtering data from a specific period onwards. It provides a summarized view of key metrics for insurance agreements.

## Data Sources (Inputs)
- ← [[galaxy.agree_prod_month_fact_agg]]
| Column Name |
|---|
| period_month_key |
| AGREE_PRODUCT_QTY_OB |
| AGREE_PRODUCT_QTY_CB |
| AGREE_PRODUCT_QTY_NC |
| agreement_offer_key |
| agreement_product_key |
| market_area_key |
- ← [[galaxy.agreement_offer_dim]]
| Column Name |
|---|
| agreement_offer_key |
| agreement_offer_name |
- ← [[galaxy.agreement_product_dim_v]]
| Column Name |
|---|
| product_key |
| product_name |
| DRM_COMMON_MARKET_PRODUCT |

