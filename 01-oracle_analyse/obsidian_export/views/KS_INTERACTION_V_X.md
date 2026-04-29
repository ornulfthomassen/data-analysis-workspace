# KS_INTERACTION_V_X

**Schema:** `CCM` | **Type:** `View`

## Description
This view constructs a detailed, time-series record of individual customer interaction segments, enriching core interaction data with agent, resource, queue, and custom user-defined details. It standardizes interaction timestamps (start, end, and estimated next interaction start for the same agent) by accounting for daylight savings. The view integrates various dimensions such as organizational structure (team, unit, site, company) and interaction metadata (type, media, technical results), along with numerous custom attributes. It also includes metrics like interaction duration, handle counts, and customer wait/hold/dial/ring durations, and filters for specific media types and valid interaction segments. This comprehensive dataset is designed for in-depth analysis of contact center operations and customer journey, and is processed incrementally based on load date.

## Data Sources (Inputs)
- ← [[KS_STAGING.INTERACTION_FACT]]
| Column Name |
|---|
| START_DATE_TIME_KEY |
| INTERACTION_ID |
| INTERACTION_TYPE_KEY |
| MEDIA_TYPE_KEY |
| SOURCE_ADDRESS |
| TARGET_ADDRESS |
| LOAD_DATE |
- ← [[CRM_ANALYSE.KS_INTERACTION_LOAD_LOG_V]]
| Column Name |
|---|
| MAX_LOAD_DATE |
- ← [[KS_STAGING.INTERACTION_RESOURCE_FACT]]
| Column Name |
|---|
| START_TS |
| END_TS |
| INTERACTION_RESOURCE_ID |
| INTERACTION_RESOURCE_ORDINAL |
| INTERACTION_ID |
| MEDIATION_SEGMENT_ID |
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
- ← [[KS_STAGING.DATE_TIME]]
| Column Name |
|---|
| DATE_TIME_KEY |
| CAL_DATE |
- ← [[RSSHUGIN.DIM_CALENDAR_WORKDAY]]
| Column Name |
|---|
| date |
| summer_time |
- ← [[KS_STAGING.INTERACTION_TYPE1]]
| Column Name |
|---|
| INTERACTION_TYPE_KEY |
| INTERACTION_TYPE_CODE |
- ← [[KS_STAGING.MEDIA_TYPE]]
| Column Name |
|---|
| MEDIA_TYPE_KEY |
| MEDIA_NAME |
- ← [[KS_STAGING.RESOURCE_]]
| Column Name |
|---|
| RESOURCE_KEY |
| RESOURCE_TYPE |
| EMPLOYEE_ID |
| RESOURCE_NAME |
- ← [[KS_STAGING.TECHNICAL_DESCRIPTOR]]
| Column Name |
|---|
| TECHNICAL_DESCRIPTOR_KEY |
| TECHNICAL_RESULT |
| RESULT_REASON |
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
| KURT_ID_OWNER |
| KURT_ID_USER |
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
- ← [[KS_READER.DIM_QUEUE_RM_V]]
| Column Name |
|---|
| QUEUE_SHORTNAME |
| QUEUE_CLIENT |
| QUEUE_PROGRAM |
| QUEUE_TYPE |

