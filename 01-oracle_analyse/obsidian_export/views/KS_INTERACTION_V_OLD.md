# KS_INTERACTION_V_OLD

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates a wide range of interaction-related data, including agent, queue, customer, and system details, from various staging and dimensional tables. It provides comprehensive information for analytical or reporting purposes, potentially focusing on recent interactions based on the `LOAD_DATE` filtering. It combines core interaction facts with resource, media, technical, user-defined custom data, and organizational dimensions (employees, teams, units, sites, companies).

## Data Sources (Inputs)
- ← [[KS_STAGING.INTERACTION_FACT]]
| Column Name |
|---|
| START_TS |
| END_TS |
| INTERACTION_ID |
| SOURCE_ADDRESS |
| TARGET_ADDRESS |
| INTERACTION_TYPE_KEY |
| MEDIA_TYPE_KEY |
| LOAD_DATE |
- ← [[CRM_ANALYSE.KS_INTERACTION_LOAD_LOG_V]]
| Column Name |
|---|
| MAX_LOAD_DATE |
- ← [[KS_STAGING.INTERACTION_RESOURCE_FACT]]
| Column Name |
|---|
| INTERACTION_RESOURCE_ID |
| INTERACTION_ID |
| INTERACTION_RESOURCE_ORDINAL |
| END_TS |
| START_TS |
| QUEUE_DURATION |
| HANDLE_COUNT |
| CUSTOMER_ACW_DURATION |
| CUSTOMER_HANDLE_COUNT |
| CUSTOMER_TALK_DURATION |
| MEDIA_RESOURCE_KEY |
| RESOURCE_KEY |
| TECHNICAL_DESCRIPTOR_KEY |
| CUSTOMER_HOLD_DURATION |
| CUSTOMER_HOLD_COUNT |
| CUSTOMER_DIAL_COUNT |
| CUSTOMER_DIAL_DURATION |
| CUSTOMER_RING_COUNT |
| CUSTOMER_RING_DURATION |
- ← [[KS_STAGING.MEDIATION_SEGMENT_FACT]]
| Column Name |
|---|
| MEDIATION_SEGMENT_ID |
| MEDIATION_DURATION |
| RESOURCE_KEY |
| TARGET_IXN_RESOURCE_SDT_KEY |
- ← [[KS_STAGING.INTERACTION_TYPE1]]
| Column Name |
|---|
| INTERACTION_TYPE_CODE |
| INTERACTION_TYPE_KEY |
- ← [[KS_STAGING.MEDIA_TYPE]]
| Column Name |
|---|
| MEDIA_TYPE_KEY |
| MEDIA_NAME |
- ← [[KS_STAGING.RESOURCE_]]
| Column Name |
|---|
| RESOURCE_KEY |
| EMPLOYEE_ID |
| RESOURCE_TYPE |
| RESOURCE_NAME |
- ← [[KS_STAGING.TECHNICAL_DESCRIPTOR]]
| Column Name |
|---|
| TECHNICAL_RESULT |
| RESULT_REASON |
| TECHNICAL_DESCRIPTOR_KEY |
- ← [[KS_STAGING.IRF_USER_DATA_CUST_1]]
| Column Name |
|---|
| INTERACTION_RESOURCE_ID |
| SKILL |
| DealerIdentify |
| SP_CONSULT_DONE |
| SP_TRANSFER |
| SP_CONSULT |
| XPROD |
| VPROD |
| BRUKTYP |
| connId |
- ← [[KS_STAGING.IRF_USER_DATA_CUST_2]]
| Column Name |
|---|
| INTERACTION_RESOURCE_ID |
| ANI |
| WFM_ACTIVITY |
| RINGT_SIST |
- ← [[KS_STAGING.IRF_USER_DATA_KEYS]]
| Column Name |
|---|
| INTERACTION_RESOURCE_ID |
| DIM1_FK |
| DIM2_FK |
| DIM3_FK |
- ← [[KS_STAGING.USER_DATA_CUST_DIM_1]]
| Column Name |
|---|
| ID |
| TransferReason |
| VAG_SELECTED |
| GAD_INFO |
| ORIGIN_SITE |
- ← [[KS_STAGING.USER_DATA_CUST_DIM_2]]
| Column Name |
|---|
| ID |
| CBType |
| B_NUMBER |
| called_service |
| FailedReason |
- ← [[KS_STAGING.USER_DATA_CUST_DIM_3]]
| Column Name |
|---|
| ID |
| BEDTYP |
| ALDERKAT |
- ← [[KS_STAGING.USER_DATA_CUST_DIM_4]]
| Column Name |
|---|
| ID |
| SCREENING_RESULT |
- ← [[KS_READER.DIM_USERS_RM]]
| Column Name |
|---|
| EMPLOYEE_NUMBER |
| HIST_FROM_DATE |
| HIST_TO_DATE |
| TEAM_ID |
| CONTRACT_ID |
- ← [[KS_READER.DIM_TEAM_RM]]
| Column Name |
|---|
| TEAM_ID |
| TEAM_NUMBER |
| UNIT_ID |
- ← [[KS_READER.DIM_UNIT_RM]]
| Column Name |
|---|
| UNIT_ID |
| UNIT_NUMBER |
| SITE_ID |
- ← [[KS_READER.DIM_SITE_RM]]
| Column Name |
|---|
| SITE_ID |
| SITE_NAME |
| COMPANY_ID |
- ← [[KS_READER.DIM_COMPANY_RM]]
| Column Name |
|---|
| COMPANY_ID |
| COMPANY_NAME |
- ← [[KS_READER.DIM_USERCONTRACT_RM]]
| Column Name |
|---|
| CONTRACTID |

