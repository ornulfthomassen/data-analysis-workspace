# VYA_ODS_OTT_MIN_SKY_HIST

**Schema:** `CCM` | **Type:** `View`

## Description
This view, 'VYA_ODS_OTT_MIN_SKY_HIST', calculates and consolidates historical usage metrics for the 'Min Sky' Over-The-Top (OTT) service. It combines detailed user activity and quota information with customer mapping data to provide a unified historical record of service usage, including foreground activity, connection status, and media file counts, linked to customer and user IDs.

## Data Sources (Inputs)
- ← [[CLM_ADM.SCD2_MIN_SKY_MAIN]]
| Column Name |
|---|
| USER_ID |
| LAST_FOREGROUND_DATE |
| LAST_CONNECTION_DTTM |
| CREATION_DTTM |
| TOTAL_QUOTA |
| USED_QUOTA |
| MEDIA_FILE_COUNT |
| OPT_OUT_PROD_IMPROVMNT_ANALTCS |
| ON_LAST_FILE |
| CURRENT_RECORD |
- ← [[ODS.CONNECT_ID_LINK]]
| Column Name |
|---|
| USER_ID |
| RANK_CONNECTION |
| ACTIVE_FLAG |
| CUSTOMER_ID |
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |

