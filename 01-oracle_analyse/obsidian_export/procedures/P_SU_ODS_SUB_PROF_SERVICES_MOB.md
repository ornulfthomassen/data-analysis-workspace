# P_SU_ODS_SUB_PROF_SERVICES_MOB

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This procedure orchestrates the refresh and update of the ODS_SUB_PROF_SERVICES_MOB table. It constructs a new version of the table (`ODS_SUB_PROF_SERVICES_MOB_N`) by joining various data sources to gather subscription profile information, including customer demographics, historical product offers, data boost statistics, and twin SIM card details. It first creates a temporary work table (`WORK_ACTIVE_SUBSCR_MOB`) to pre-process subscription and customer data. After populating `ODS_SUB_PROF_SERVICES_MOB_N` and building its indexes, it performs a row count comparison against the existing `ODS_SUB_PROF_SERVICES_MOB` table. If the row count difference is within a predefined threshold, it performs a 'table swap' by renaming the current `ODS_SUB_PROF_SERVICES_MOB` to `ODS_SUB_PROF_SERVICES_MOB_O` (as a backup) and then renaming `ODS_SUB_PROF_SERVICES_MOB_N` to `ODS_SUB_PROF_SERVICES_MOB`. Finally, it adjusts index names and grants permissions. Error and warning messages are logged to CLM_CCM.CCM_LOAD_HISTORY.

## Data Sources (Inputs)
- ← [[CLM_CCM.ODS_SUB_PROF_SERVICES_MOB]]
- ← [[CLM_CCM.ODS_SUBSCRIPTION_MV]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SRC_SUBSCRIPTION_ID_1 |
| MAIN_NUMBER |
| KURT_ID_USER |
| BUSINESS_AREA_ID |
| MARKET_AREA_ID |
- ← [[ODS.CUSTOMER_ODS]]
| Column Name |
|---|
| CUSTOMER_ID |
| CUSTOMER_FIRST_NAME |
| CUSTOMER_AGE |
| DATE_OF_BIRTH |
| CUSTOMER_TYPE_ID |
| CUSTOMER_STATUS_ID |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SUBSCR_START_REASON |
| MARKET_AREA_START |
| ORIGINAL_START_DATE_ORIG |
- ← [[CM.SUBSCRIPTION_OFFER_INCENTIVE]]
| Column Name |
|---|
| SUBSCR_ID |
| PRODUCT_OFFER_ID |
| INC_VALID_TO_DATE |
| INC_VALID_FROM_DATE |
| INFO_CHG_DATE |
- ← [[PCAT.COMPONENT]]
| Column Name |
|---|
| COMPONENT_ID |
| SYSTEM_COMPONENT_TYPE |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME_USE |
| SOURCE_PRODUCT_ID_1 |
| SOURCE_SYSTEM_NAME |
| PRODUCT_NAME |
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PRODUCT_OFFER_ID |
| BUSINESS_AREA_ID |
| START_DATE |
| END_DATE |
- ← [[ODS.SUBSCRIBED_OFFER_ODS_MOB]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PRODUCT_OFFER_ID |
| MAIN_NUMBER |
| SUB_NUMBER |
- ← [[ODS.SUBSCRIPTION_ODS_MOB]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| CUSTOMER_ROLE_ID |
| MARKET_AREA_ID |
| MAIN_NUMBER |
- ← [[CRM_ANALYSE.PD]]
| Column Name |
|---|
| PRODUCT_KEY |
| DRM_COMMON_MARKET_PRODUCT |
| PRODUCT_FAMILY_NAME |

## Target Tables (Outputs)
- → [[CLM_CCM.WORK_ACTIVE_SUBSCR_MOB]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SRC_SUBSCRIPTION_ID_1 |
| SUSCR_ID |
| MAIN_NUMBER |
| KURT_ID_USER |
| BUSINESS_AREA_ID |
| MARKET_AREA_ID |
| CUST_USER_FIRST_NAME |
| CUST_USER_AGE |
| CUST_USER_NBR_DAYS_NEXT_BDAY |
- → [[CLM_CCM.ODS_SUB_PROF_SERVICES_MOB_N]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SUBSCR_START_REASON |
| SUBSCR_MARKET_AREA_START |
| SUBSCR_ORIGINAL_START_DATE_ORIG |
| SUBSCR_NBR_DAYS_ACTIVE |
| PRODUCT_OFFER_ID_PREV |
| END_DATE_PREV |
| NBR_DAYS_ACTIVE_PREV |
| DP_BOOST_NBR_365D |
| DP_BOOST_MIN_START_DATE |
| DP_BOOST_MAX_START_DATE |
| NBR_TWINS_DATA |
| NBR_TWINS_SPEECH |
| NBR_TWINS_UNCLASSIFIED |
| CUST_USER_FIRST_NAME |
| CUST_USER_AGE |
| CUST_USER_NBR_DAYS_NEXT_BDAY |
- → [[CLM_CCM.ODS_SUB_PROF_SERVICES_MOB_O]]
- → [[CLM_CCM.ODS_SUB_PROF_SERVICES_MOB]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SUBSCR_START_REASON |
| SUBSCR_MARKET_AREA_START |
| SUBSCR_ORIGINAL_START_DATE_ORIG |
| SUBSCR_NBR_DAYS_ACTIVE |
| PRODUCT_OFFER_ID_PREV |
| END_DATE_PREV |
| NBR_DAYS_ACTIVE_PREV |
| DP_BOOST_NBR_365D |
| DP_BOOST_MIN_START_DATE |
| DP_BOOST_MAX_START_DATE |
| NBR_TWINS_DATA |
| NBR_TWINS_SPEECH |
| NBR_TWINS_UNCLASSIFIED |
| CUST_USER_FIRST_NAME |
| CUST_USER_AGE |
| CUST_USER_NBR_DAYS_NEXT_BDAY |
- → [[CLM_CCM.CCM_LOAD_HISTORY]]
| Column Name |
|---|
| TABLE_NAME |
| START_DTTM |
| STATUS |
| ERROR_MESSAGE |
| WF_NAME |
| S_NAME |

