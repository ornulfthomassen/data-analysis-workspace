# SAFESEC_ID_THEFT_WEEKLY

**Schema:** `CCM` | **Type:** `View`

## Description
This view is designed for a weekly load of ID theft insurance data, specifically for policies sold through dealers and not part of the 'SAFE' system, into the Viya platform. It retrieves detailed agreement, customer, product, and dealer information, filtering for specific product IDs (53029 and 771) and valid agreement date ranges, associating each record with a specific reporting week.

## Data Sources (Inputs)
- ← [[ods.agreement_ods_mob]]
- ← [[galaxy.product_dim]]
- ← [[clm_adm.adm_customer_mapping]]
- ← [[galaxy.date_dim_mv]]
- ← [[onl_rep.agreement_order_offer]]
- ← [[ONL_REP.agreement_order]]
- ← [[galaxy.dealer_dim]]

