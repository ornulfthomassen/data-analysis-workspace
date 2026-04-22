# V_SAFE_AGREEMENT

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a consolidated and enriched overview of agreement products, including their status, start and end dates. It identifies active products using a `product_act_flag` and links agreement product information with customer details (owner, lifecycle segment) and dealer information.

## Data Sources (Inputs)
- ← [[clm_ccm.v_ods_agrmt_offer_mob_safety]]
- ← [[onl_rep.agreement_order_offer]]
- ← [[onl_rep.agreement_order]]
- ← [[CLM_ADM.adm_customer_mapping]]
- ← [[GALAXY.dealer_dim]]
- ← [[CLM_CCM.ccm_customer_info_2]]

