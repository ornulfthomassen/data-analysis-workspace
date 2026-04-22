# THEA_TEST_AGREEMENT

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates various agreement and product quantities (opening balance, new, closing balance) by period month, agreement offer name, product name, and market area. It specifically filters for data from period month 202200 onwards and for agreement offers whose names contain 'Sikkerhetsprodukter'. The purpose is to provide a summarized view of security-related product and agreement metrics over time.

## Data Sources (Inputs)
- ← [[galaxy.agree_prod_month_fact_agg]]
- ← [[galaxy.agreement_offer_dim]]
- ← [[galaxy.agreement_product_dim_v]]

