# TMP_THEA_FORSIKRING

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates agreement product quantities (opening balance, closing balance, new contracts) for insurance-related products from January 2022 onwards. The data is grouped by period month, agreement offer name, product name, and market area.

## Data Sources (Inputs)
- ← [[galaxy.agree_prod_month_fact_agg]]
- ← [[galaxy.agreement_offer_dim]]
- ← [[galaxy.agreement_product_dim_v]]

