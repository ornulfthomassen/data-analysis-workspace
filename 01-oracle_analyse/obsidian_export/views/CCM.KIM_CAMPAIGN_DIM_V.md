# KIM_CAMPAIGN_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, 'KIM_CAMPAIGN_DIM_V', serves as a dimension view for campaign-related data. It directly selects all columns from the 'KIM_CAMPAIGN_DIM' table, applying data type casting and length restrictions to various VARCHAR2 columns to standardize their format for consistency and potential data warehousing purposes.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DIM]]
| Column Name |
|---|
| CAMPAIGN_KEY |
| SOURCE_SYSTEM_KEY |
| CAMPAIGN_SK |
| CAMPAIGN_CD |
| CAMPAIGN_STATUS_CD |
| CAMPAIGN_VERSION_NO |
| CURRENT_VERSION_FLG |
| CAMPAIGN_NM |
| CAMPAIGN_DESC |
| CAMPAIGN_FOLDER_TXT |
| CAMPAIGN_OWNER_NM |
| CAMPAIGN_GROUP_SK |
| START_DTTM |
| END_DTTM |
| RUN_DTTM |
| LAST_MODIFIED_DTTM |
| LAST_MODIFIED_BY_USER_NM |
| APPROVAL_DTTM |
| APPROVAL_GIVEN_BY_NM |
| BUSINESS_CONTEXT_NM |
| CAMPAIGN_TYPE_CD |
| DELETED_FLG |
| COMM_PLATFORM |
| ACTIVITY_AREA |
| PARENT_CAMPAIGN_CODE |
| CAMPAIGN_DOCUMENTATION |
| CAMPAIGN_MANAGER |
| CAMPAIGN_STATUS |
| SCHEDULED_WORK_START_DATE |
| APPROVED_REQUIRED_DATE |
| APPROVED_BY |
| START_DATE |
| END_DATE |
| CURRENT_STATUS |
| VALUE_NAME |
| CAMPAIGN_TYPE_DESC |


