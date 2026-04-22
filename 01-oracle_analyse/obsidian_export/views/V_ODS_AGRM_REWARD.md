# V_ODS_AGRM_REWARD

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive, consolidated dataset for 'Familiebonus-medlem' (Family Bonus Member) agreements. It combines agreement details, specific reward information (both detailed and aggregated), and maps agreement owners and members to their respective customer keys. The view calculates active/inactive statuses for both agreements and members, and identifies whether a member is an 'invitee' (i.e., distinct from the agreement owner). It aims to offer a unified perspective on these specific types of agreements and their reward entitlements.

## Data Sources (Inputs)
- ← [[clm_ccm.v_ods_agrmt_mob]]
- ← [[clm_ccm.v_ods_agrmt_mob_reward_det]]
- ← [[clm_adm.adm_customer_mapping]]
- ← [[clm_ccm.v_ods_agrmt_mob_reward_agg]]

