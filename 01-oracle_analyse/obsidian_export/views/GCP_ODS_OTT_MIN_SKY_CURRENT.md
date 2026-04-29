# GCP_ODS_OTT_MIN_SKY_CURRENT

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates 'Min Sky' service usage metrics per customer, providing consolidated activity dates, foreground/connection duration sums over various periods, total and used quota, media file counts, and opt-out preferences, by linking user data to customer IDs.

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

