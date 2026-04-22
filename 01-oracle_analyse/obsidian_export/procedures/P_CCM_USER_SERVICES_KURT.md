# P_CCM_USER_SERVICES_KURT

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure collects and consolidates user account, phone, and service verification data from various source systems (Comoyo FIM, Galaxy, and CLM_CCM). It processes 'hardlink' identifiers to derive 'KURT_ID's, matches users with their phone numbers and associated service providers, and aggregates verification sources. The script ultimately creates a series of temporary tables to build a comprehensive view of user identities and their service origins, culminating in a table that assigns a 'QA_flag' based on customer type and verification sources. The procedure appears to be a data preparation or integration routine for user service data analysis or quality assurance.

## Data Sources (Inputs)
- ← [[COMOYO.FIM_USER_ACCOUNTS]]
- ← [[COMOYO.FIM_USER_PHONES]]
- ← [[COMOYO.USER_SERVICES_SERVICE_SCD]]
- ← [[galaxy.subscription_dim_mv]]
- ← [[galaxy.subscr_detail_fact]]
- ← [[clm_ccm.ccm_customer]]
- ← [[ccm_phones_cm_tmp]]

## Target Tables (Outputs)
- → [[CCM_HARDLINK_TMP]]
- → [[CCM_USERS_SDMV_TMP]]
- → [[CCM_USER_KURT_SAMMEN_TMP]]
- → [[CCM_USER_PHONE_KILDE_TMP]]
- → [[CCM_USER_KURT_KILDE_TMP]]
- → [[CCM_USER_KURT_KILDE_CP]]
- → [[CCM_USERS_TMP]]
- → [[CCM_PHONES_TMP]]

