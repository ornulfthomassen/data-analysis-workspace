# P_CCM_AGREEMENT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Processes various types of customer agreements (SWAP, Familiebonus, Sikker ID) by extracting and transforming data from multiple source systems, enriching it with product and customer details, and then consolidating the agreement and agreement member information into staging tables. It also logs the execution status and drops/recreates temporary tables to ensure data freshness.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
- ← [[DUAL]]
- ← [[CM.AGREEMENT_OFFER]]
| Column Name |
|---|
| agreement_offer_id |
| agreement_id |
| valid_from_date |
| valid_to_date |
| product_offer_id |
| info_is_deleted |
| agreement_offer_id_parent |
- ← [[GALAXY.AGREEMENT_DIM]]
| Column Name |
|---|
| source_system_agreement_id_1 |
| agreement_offer_name |
| agreement_key |
| agreement_owner_key |
| agreement_start_dt_key |
| agreement_end_dt_key |
| agreement_offer_key |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| source_product_id_1 |
| product_key |
| product_desc |
| drm_common_product_group |
| product_name |
| source_system_name |
- ← [[CM.AGREEMENT_OFFER_CONFIGURATION]]
| Column Name |
|---|
| agreement_offer_id |
| parameter_value |
| parameter_id |
| info_is_deleted |
| valid_to_date |
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
| Column Name |
|---|
| order_id |
| order_phone_num |
| subscr_id |
| order_line_id |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| source_system_key |
| subscription_id |
| source_system_id |
- ← [[CM.AGREEMENT_OWNER]]
| Column Name |
|---|
| agreement_id |
| master_id |
| valid_from_date |
| valid_to_date |
- ← [[GALAXY.CUSTOMER_DIM]]
| Column Name |
|---|
| master_id |
| customer_key |
- ← [[CM.AGREEMENT_MEMBER_NEW]]
| Column Name |
|---|
| agreement_id |
| master_id |
| valid_from_date |
| valid_to_date |
- ← [[AGR.BMGM_ACCESSES_KURT]]
| Column Name |
|---|
| kurt_id |
| main_number |
| sk_product_offer_id |
| product_name |
| num_priv_postpaid_subs_owned |
| num_bus_postpaid_subs_used |
| num_swap_agreements_owned |
| num_mbb_subs_owned |
| num_fixed_broadband_owned |
| num_fixed_telephony_subs_owned |
| mob_subscr_id |
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
| Column Name |
|---|
| subscription_key |
| owner_customer_key |
| user_customer_key |
| prim_prod_start_dt_key |
| prim_prod_end_dt_key |
| prim_product_key |
| subscr_type_status_key |
| market_area_key |
| sub_product_key |
| sub_prod_end_dt_key |
- ← [[GALAXY.PRIMARY_PRODUCT_DIM_V]]
| Column Name |
|---|
| prim_product_key |
| prim_product_desc |
- ← [[LIVE.EUREKA_IMEI]]
| Column Name |
|---|
| imei |
| directory_number_id |
| terminal_use_first_date |
| terminal_use_last_date |
| subscr_id |
- ← [[GALAXY.SUBSCRIPTION_DIM_MV]]
| Column Name |
|---|
| subscription_key |
| main_number |
- ← [[GALAXY.MARKET_AREA_DIM]]
| Column Name |
|---|
| market_area_key |
- ← [[TMP_SWAP_UTG]]
| Column Name |
|---|
| agreement_key |
| agreement_offer_id |
| memb_valid_from_date |
| memb_valid_to_date |
| order_phone_num |
| subscription_key |
| product_key |
| product_desc |
| imei |
| source_agreement_id |
| agreement_offer_name |
| agreement_owner_key |
| valid_from_date |
| valid_to_date |
- ← [[TMP_FB_UTG]]
| Column Name |
|---|
| agreement_key |
| agreement_offer_id |
| kurt_id_member |
| member_from |
| member_to |
| subscription_key |
| main_number |
| avt_rank |
| product_key |
| product_name |
| fb_grunnlag |
| fb_brukere |
| source_agreement_id |
| agreement_offer_name |
| kurt_id_owner |
| valid_from_date |
| valid_to_date |
- ← [[TMP_SIKKER_ID_UTG]]
| Column Name |
|---|
| AGREEMENT_KEY |
| AGREEMENT_OFFER_ID |
| KURT_ID_MEMBER |
| MEMBER_FROM |
| MEMBER_TO |
| SUBSCRIPTION_KEY |
| MAIN_NUMBER |
| AVT_RANK |
| SOURCE_AGREEMENT_ID |
| AGREEMENT_OFFER_NAME |
| KURT_ID_OWNER |
| VALID_FROM_DATE |
| VALID_TO_DATE |
- ← [[TMP_SWAP_UTG_MEDL0]]
| Column Name |
|---|
| subscription_key |
| owner_customer_key |
| user_customer_key |
| prim_prod_start |
| prim_prod_end |
| prim_product_key |
| prim_product_desc |
- ← [[TMP_SWAP_UTG_MEDL1]]
| Column Name |
|---|
| imei |
| agreement_key |
| agreement_offer_id |
| kurt_id_member |
| memb_valid_from_date |
| memb_valid_to_date |
| main_number_agr |
| subscription_key_agr |
| prim_product_key |
| prim_product_desc |
| product_key |
| product_desc |
- ← [[TMP_SWAP_UTG_MEDL2]]
| Column Name |
|---|
| imei |
| terminal_use_last_date |
| terminal_use_first_date |
| main_number_use |
- ← [[TMP_FB_AKTIVERING]]
| Column Name |
|---|
| main_number |
- ← [[TMP_FB_UTG_MEDL]]
| Column Name |
|---|
| agreement_key |
| agreement_offer_id |
| kurt_id_member |
| memb_valid_from_date |
| memb_valid_to_date |
| imei |
| terminal_use_last_date |
| subscription_key_agr |
| main_number_agr |
| product_key |
| product_desc |
| fb_grunnlag |
| fb_brukere |
| fb_aktivert |
- ← [[TMP_SIKKER_ID_UTG_MEDL]]
| Column Name |
|---|
| AGREEMENT_KEY |
| AGREEMENT_OFFER_ID |
| KURT_ID_MEMBER |
| MEMB_VALID_FROM_DATE |
| MEMB_VALID_TO_DATE |
| SUBSCRIPTION_KEY_AGR |
| MAIN_NUMBER_AGR |
| SIKKER_ID_AKTIVERT |
| RANK |

## Target Tables (Outputs)
- → [[P_CCM_AGREEMENT_LOG]]
| Column Name |
|---|
| Steg |
| status |
| tid |
- → [[TMP_SWAP_UTG]]
| Column Name |
|---|
| agreement_offer_id |
| agreement_offer_name |
| agreement_key |
| source_agreement_id |
| agreement_owner_key |
| product_key |
| product_desc |
| valid_from_date |
| valid_to_date |
| Memb_valid_from_date |
| memb_valid_to_date |
| imei |
| source_order_id |
| device_agreement_status |
| order_phone_num |
| subscription_key |
- → [[TMP_FB_UTG]]
| Column Name |
|---|
| agreement_offer_id |
| agreement_offer_name |
| agreement_key |
| source_agreement_id |
| kurt_id_owner |
| valid_from_date |
| valid_to_date |
| imei |
| kurt_id_member |
| main_number |
| subscription_key |
| member_from |
| member_to |
| product_key |
| product_name |
| fb_grunnlag |
| fb_brukere |
| avt_rank |
- → [[TMP_SIKKER_ID_UTG]]
| Column Name |
|---|
| AGREEMENT_OFFER_ID |
| AGREEMENT_OFFER_NAME |
| AGREEMENT_KEY |
| SOURCE_AGREEMENT_ID |
| KURT_ID_OWNER |
| VALID_FROM_DATE |
| VALID_TO_DATE |
| KURT_ID_MEMBER |
| MAIN_NUMBER |
| SUBSCRIPTION_KEY |
| MEMBER_FROM |
| MEMBER_TO |
| AVT_RANK |
- → [[STG_AGREEMENT]]
| Column Name |
|---|
| period_id |
| agreement_key |
| source_agreement_id |
| agreement_offer_name |
| kurt_id_owner |
| valid_from_date |
| valid_to_date |
- → [[TMP_SWAP_UTG_MEDL0]]
| Column Name |
|---|
| subscription_key |
| owner_customer_key |
| user_customer_key |
| order_phone_num |
| subscription_key_agr |
| prim_prod_start |
| prim_prod_end |
| prim_product_key |
| prim_product_desc |
- → [[TMP_SWAP_UTG_MEDL1]]
| Column Name |
|---|
| agreement_key |
| agreement_offer_id |
| owner_customer_key |
| kurt_id_member |
| memb_valid_from_date |
| memb_valid_to_date |
| main_number_agr |
| subscription_key_agr |
| prim_prod_start |
| prim_prod_end |
| prim_product_key |
| prim_product_desc |
| product_key |
| product_desc |
| imei |
- → [[TMP_SWAP_UTG_MEDL2]]
| Column Name |
|---|
| imei |
| eureka_imei |
| main_number_use |
| terminal_use_first_date |
| terminal_use_last_date |
- → [[TMP_SWAP_UTG_MEDL3]]
| Column Name |
|---|
| imei |
| eureka_imei |
| main_number_use |
| terminal_use_first_date |
| terminal_use_last_date |
| diff |
| rank |
- → [[TMP_FB_AKTIVERING]]
| Column Name |
|---|
| main_number |
- → [[TMP_FB_UTG_MEDL]]
| Column Name |
|---|
| agreement_key |
| agreement_offer_id |
| kurt_id_member |
| memb_valid_from_date |
| memb_valid_to_date |
| imei |
| terminal_use_first_date |
| terminal_use_last_date |
| subscription_key_agr |
| main_number_agr |
| rank |
| product_key |
| product_desc |
| fb_grunnlag |
| fb_brukere |
| avt_rank |
| fb_aktivert |
- → [[TMP_SIKKER_ID_UTG_MEDL]]
| Column Name |
|---|
| AGREEMENT_KEY |
| AGREEMENT_OFFER_ID |
| KURT_ID_MEMBER |
| MEMB_VALID_FROM_DATE |
| MEMB_VALID_TO_DATE |
| SUBSCRIPTION_KEY_AGR |
| MAIN_NUMBER_AGR |
| RANK |
| AVT_RANK |
| SIKKER_ID_AKTIVERT |
- → [[STG_AGREEMENT_MEMBER]]
| Column Name |
|---|
| period_id |
| agreement_key |
| agreement_offer_id |
| kurt_id_member |
| memb_valid_from_date |
| memb_valid_to_date |
| imei |
| eureka_imei |
| terminal_use_last_date |
| used_last_30 |
| prim_product_key |
| prim_product_desc |
| product_key |
| product_desc |
| subscription_key_agr |
| main_number_agr |
| main_number_use |
| fb_grunnlag |
| fb_brukere |
| fb_aktivert |

