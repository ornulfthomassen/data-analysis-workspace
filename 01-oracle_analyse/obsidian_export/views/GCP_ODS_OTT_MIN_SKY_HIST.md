# GCP_ODS_OTT_MIN_SKY_HIST

**Schema:** `CCM` | **Type:** `View`

## Description
Consolidates and prepares historical 'Min Sky' service usage data from a Slowly Changing Dimension Type 2 (SCD2) table. It links usage metrics with customer IDs, calculates key performance indicators (KPIs) for foreground and connection activity, and provides aggregated quota and media file counts. This view is intended for analytical purposes or loading into downstream data systems like 'Mjøsa'.

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
| CUSTOMER_ID |
| USER_ID |
| RANK_CONNECTION |
| ACTIVE_FLAG |

