# V_ODS_FAMILIEBONUS

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `V_ODS_FAMILIEBONUS`, consolidates detailed information about specific mobile agreements (filtered by `src_agreement_product_id = 951`), their associated reward aggregates and details, and customer mapping information. It provides agreement metadata (ID, dates, type, status, active days), aggregated reward details (units basis, usable units, allocated sum), detailed unit-level reward information (source, product, reward basis/usable), and maps various `kurt_id`s (owner, member, user) to `customer_sk`. Additionally, it includes flags indicating the active status of the agreement and its members based on their end dates relative to the current system date. This suggests its purpose is to provide a comprehensive dataset for analyzing or reporting on a 'Family Bonus' or similar mobile agreement program.

## Data Sources (Inputs)
- ← [[clm_ccm.v_ods_agrmt_mob]]
- ← [[clm_ccm.v_ods_agrmt_mob_reward_agg]]
- ← [[clm_ccm.v_ods_agrmt_mob_reward_det]]
- ← [[ods.bmgm_accesses_kurt_ods]]
- ← [[clm_adm.adm_customer_mapping]]

