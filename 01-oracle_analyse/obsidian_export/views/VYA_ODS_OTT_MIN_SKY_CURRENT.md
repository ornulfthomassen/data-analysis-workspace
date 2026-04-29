# VYA_ODS_OTT_MIN_SKY_CURRENT

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a consolidated view of 'Min Sky' OTT service usage and quota metrics, aggregated by customer. It calculates various usage statistics (like first/last activity dates, foreground/connection sums over different periods, quota, and media file counts) per user and then maps these to a customer key.

## Data Sources (Inputs)
- ← [[CLM_ADM.SCD2_MIN_SKY_MAIN]]
| Column Name |
|---|
| USER_ID |
| CREATION_DTTM |
| LAST_FOREGROUND_DATE |
| LAST_CONNECTION_DTTM |
| CURRENT_RECORD |
| TOTAL_QUOTA |
| USED_QUOTA |
| MEDIA_FILE_COUNT |
| OPT_OUT_PROD_IMPROVMNT_ANALTCS |
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

