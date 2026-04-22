# P_CCM_USER_SERVICES_PF

**Schema:** `CCM` | **Type:** `Procedure`

## Description
The procedure dynamically creates a unique index named `uidx_us_user_service_cp_pf` on the `ccm_user_services_cp_pf` table, using the `user_id` and `service_cd` columns to enforce uniqueness. It includes error handling to report any failures during the index creation process.

