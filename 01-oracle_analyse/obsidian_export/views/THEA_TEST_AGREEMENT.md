# THEA_TEST_AGREEMENT

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates agreement and product quantities (opening balance, new contracts, closing balance) by period, agreement offer, product, and market area. It filters data for 'Sikkerhetsprodukter' agreements from period 202200 onwards.

## Data Sources (Inputs)
- ← [[galaxy.agree_prod_month_fact_agg]]
| Column Name |
|---|
| period_month_key |
| agree_qty_ob |
| agree_qty_nc |
| agree_qty_cb |
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

