# P_CCM_USER_SERVICES_PF

**Schema:** `CCM` | **Type:** `Procedure`

## Description
The procedure dynamically creates a unique index named 'uidx_us_user_service_cp_pf' on the 'ccm_user_services_cp_pf' table. This index is built upon the 'user_id' and 'service_cd' columns, enforcing uniqueness for combinations of these values and potentially improving data retrieval performance. The procedure includes robust error handling to catch and report any issues during the index creation.

## Data Sources (Inputs)
- ← [[ccm_user_services_cp_pf]]
| Column Name |
|---|
| user_id |
| service_cd |

