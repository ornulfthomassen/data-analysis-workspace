# P_CU_ODS_CUSTOMER_PROF

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Generates and maintains a comprehensive customer profile dataset (`ODS_CUSTOMER_PROF`) by consolidating data from various ODS and DWH sources. It calculates and aggregates customer attributes such as demographic information (gender), credit status, portal usage metrics (Mitt Telenor, Minesider), detailed subscription activity (number of active mobile and broadband subscriptions for owners/users), and telemarketing contact rankings (household, GAB flat, GAB number). The procedure uses an atomic table swap mechanism to ensure data availability and consistency, building new data in a temporary table (`ODS_CUSTOMER_PROF_N`) and then renaming it to become the main table, while potentially retaining the old main table as a backup (`ODS_CUSTOMER_PROF_O`). It also includes robust logging for execution status and error handling.

## Data Sources (Inputs)
- ← [[ODS.CUSTOMER_ODS]]
| Column Name |
|---|
| CUSTOMER_ID |
| DATE_OF_BIRTH |
| CUSTOMER_STATUS_ID |
| CUSTOMER_TYPE_ID |
| CUSTOMER_AGE |
| HOUSEHOLD_ID |
- ← [[CCDW.CUST_FAIL_CREDIT]]
| Column Name |
|---|
| KURT_ID |
| LOAD_DTM |
| DELETED_DTM |
- ← [[GALAXY.CUSTOMER_DIM]]
| Column Name |
|---|
| CUSTOMER_KEY |
| MINE_SIDER_FLG |
| MINE_SIDER_LAST_USED |
| MITT_TELENOR_FLG |
| MITT_TELENOR_LAST_USED |
| GENDER |
| CUSTOMER_TYPE_ID |
| CUSTOMER_STATUS_ID |
- ← [[ODS.CUSTOMER_RES_AND_APP]]
| Column Name |
|---|
| CUSTOMER_ID |
| TM_IND_BR |
| TM_IND_INTERNAL |
- ← [[CLM_CCM.ODS_CUST_CONTACT_PHONE]]
| Column Name |
|---|
| KURT_ID |
| CONTACT_PHN |
| RANK_CONTACT_PHN |
- ← [[CCDW.HOUSEHOLD_MEMBER]]
| Column Name |
|---|
| CUSTOMER_ID |
| HOUSEHOLD_ID |
| GEOGRAPHY_ID |
- ← [[CLM_CCM.ODS_FAR_GROUP]]
| Column Name |
|---|
| GAB_NUMBER |
| GAB_FLAT |
| FARID |
- ← [[ODS.SUBSCRIPTION_ODS_MOB]]
| Column Name |
|---|
| CUSTOMER_ID |
| CUSTOMER_ROLE_ID |
| SUBSCR_PRODUCT_OFFER_ID |
| MARKET_AREA_ID |
- ← [[ODS.SUBSCRIPTION_ODS_FTV]]
| Column Name |
|---|
| CUSTOMER_ID |
| CUSTOMER_ROLE_ID |
| SUBSCR_PRODUCT_OFFER_ID |
| MARKET_AREA_ID |
- ← [[ODS.SUBSCRIPTION_ODS_FIXED]]
| Column Name |
|---|
| CUSTOMER_ID |
| CUSTOMER_ROLE_ID |
| SUBSCR_PRODUCT_OFFER_ID |
| MARKET_AREA_ID |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| DRM_COMMON_REPORTING |
| DRM_COMMON_SERVICE |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_TECHNOLOGY |
| PRODUCT_NAME_USE |
- ← [[ALL_TABLES]]
| Column Name |
|---|
| owner |
| table_name |
| num_rows |
- ← [[ALL_INDEXES]]
| Column Name |
|---|
| OWNER |
| TABLE_NAME |
| INDEX_NAME |
- ← [[USER_INDEXES]]
| Column Name |
|---|
| INDEX_NAME |
| TABLE_NAME |
| TABLE_OWNER |
| GENERATED |
- ← [[DUAL]]

## Target Tables (Outputs)
- → [[ODS_CUSTOMER_PROF_N]]
| Column Name |
|---|
| LOAD_DTTM |
| KURT_ID |
| GENDER |
| CREDIT_STATUS_INTERNAL_FLG |
| MITT_TELENOR_AC_FLG |
| MITT_TELENOR_ACC_MAX_LOGGED_IN |
| MINESIDER_ACC |
| MINESIDER_ACC_MAX_LOGGED_INN |
| NO_ACTIVE_MOBILE_OWNER |
| NO_ACTIVE_MOBILE_USER |
| NO_ACTIVE_BB_OWNER |
| NO_ACTIVE_BB_USER |
| TM_QUALIFIED |
| RANK_HH_TM_CONTACT |
| RANK_GAB_FLAT_TM_CONTACT |
| RANK_GAB_TM_CONTACT |
| DAYS_UNTIL_BDAY |
- → [[ODS_CUSTOMER_PROF]]
| Column Name |
|---|
| LOAD_DTTM |
| KURT_ID |
| GENDER |
| CREDIT_STATUS_INTERNAL_FLG |
| MITT_TELENOR_AC_FLG |
| MITT_TELENOR_ACC_MAX_LOGGED_IN |
| MINESIDER_ACC |
| MINESIDER_ACC_MAX_LOGGED_INN |
| NO_ACTIVE_MOBILE_OWNER |
| NO_ACTIVE_MOBILE_USER |
| NO_ACTIVE_BB_OWNER |
| NO_ACTIVE_BB_USER |
| TM_QUALIFIED |
| RANK_HH_TM_CONTACT |
| RANK_GAB_FLAT_TM_CONTACT |
| RANK_GAB_TM_CONTACT |
| DAYS_UNTIL_BDAY |
- → [[ODS_CUSTOMER_PROF_O]]
| Column Name |
|---|
| LOAD_DTTM |
| KURT_ID |
| GENDER |
| CREDIT_STATUS_INTERNAL_FLG |
| MITT_TELENOR_AC_FLG |
| MITT_TELENOR_ACC_MAX_LOGGED_IN |
| MINESIDER_ACC |
| MINESIDER_ACC_MAX_LOGGED_INN |
| NO_ACTIVE_MOBILE_OWNER |
| NO_ACTIVE_MOBILE_USER |
| NO_ACTIVE_BB_OWNER |
| NO_ACTIVE_BB_USER |
| TM_QUALIFIED |
| RANK_HH_TM_CONTACT |
| RANK_GAB_FLAT_TM_CONTACT |
| RANK_GAB_TM_CONTACT |
| DAYS_UNTIL_BDAY |
- → [[ODS_CUSTOMER_PROF_O_TEM]]
| Column Name |
|---|
| LOAD_DTTM |
| KURT_ID |
| GENDER |
| CREDIT_STATUS_INTERNAL_FLG |
| MITT_TELENOR_AC_FLG |
| MITT_TELENOR_ACC_MAX_LOGGED_IN |
| MINESIDER_ACC |
| MINESIDER_ACC_MAX_LOGGED_INN |
| NO_ACTIVE_MOBILE_OWNER |
| NO_ACTIVE_MOBILE_USER |
| NO_ACTIVE_BB_OWNER |
| NO_ACTIVE_BB_USER |
| TM_QUALIFIED |
| RANK_HH_TM_CONTACT |
| RANK_GAB_FLAT_TM_CONTACT |
| RANK_GAB_TM_CONTACT |
| DAYS_UNTIL_BDAY |
- → [[CLM_CCM.ODS_PROCEDURE_SWAP_STATUS]]
| Column Name |
|---|
| PROC_NAME |
| STATUS_DTTM |
| MESSAGE |
| OLD_ROW_COUNT |
| NEW_ROW_COUNT |
- → [[CLM_CCM.CCM_LOAD_HISTORY]]
| Column Name |
|---|
| TABLE_NAME |
| LOAD_START_DTTM |
| STATUS |
| ERROR_MESSAGE |
| POWERCENTER_WF_NAME |
| POWERCENTER_S_NAME |

