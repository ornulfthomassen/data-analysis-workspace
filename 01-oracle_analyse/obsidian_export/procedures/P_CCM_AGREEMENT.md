# P_CCM_AGREEMENT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `P_CCM_AGREEMENT` processes and consolidates different types of customer agreements (SWAP, Familiebonus, and Sikker ID). It extracts agreement details, owner and member information, product and subscription data, and usage metrics from various source systems. Intermediate temporary tables are used for calculations and data enrichment before the final aggregated agreement and agreement member data are stored in persistent staging tables (`STG_AGREEMENT` and `STG_AGREEMENT_MEMBER`). The procedure also logs its execution steps to `P_CCM_AGREEMENT_LOG`.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
- ← [[agr.bmgm_accesses_kurt]]
- ← [[ccdw.subscription_mapping]]
- ← [[cm.agreement_Owner]]
- ← [[cm.agreement_member_new]]
- ← [[cm.agreement_offer]]
- ← [[cm.agreement_offer_configuration]]
- ← [[dual]]
- ← [[galaxy.agreement_dim]]
- ← [[galaxy.customer_dim]]
- ← [[galaxy.market_area_dim]]
- ← [[galaxy.primary_product_dim_v]]
- ← [[galaxy.product_dim]]
- ← [[galaxy.subscr_detail_fact]]
- ← [[galaxy.subscription_dim_mv]]
- ← [[live.eureka_imei]]
- ← [[onl_rep.service_order_product]]

## Target Tables (Outputs)
- → [[P_CCM_AGREEMENT_LOG]]
- → [[STG_AGREEMENT]]
- → [[STG_AGREEMENT_MEMBER]]
- → [[TMP_FB_AKTIVERING]]
- → [[TMP_FB_UTG]]
- → [[TMP_FB_UTG_MEDL]]
- → [[TMP_SIKKER_ID_UTG]]
- → [[TMP_SIKKER_ID_UTG_MEDL]]
- → [[TMP_SWAP_UTG]]
- → [[TMP_SWAP_UTG_MEDL0]]
- → [[TMP_SWAP_UTG_MEDL1]]
- → [[TMP_SWAP_UTG_MEDL2]]
- → [[TMP_SWAP_UTG_MEDL3]]

