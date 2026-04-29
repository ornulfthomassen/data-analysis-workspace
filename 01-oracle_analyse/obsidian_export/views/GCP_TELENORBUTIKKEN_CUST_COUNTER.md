# GCP_TELENORBUTIKKEN_CUST_COUNTER

**Schema:** `CCM` | **Type:** `View`

## Description
Provides anonymized Telenorbutikken sales and event details for GCP, combining data from the `MAZE_STAGE` table with dealer dimension attributes from `DEALER_DIM`, and filtering for events within the last three years.

## Data Sources (Inputs)
- ← [[THIRD_PARTY_SERVICES.MAZE_STAGE]]
| Column Name |
|---|
| SYNCID |
| PARENT |
| VALUE |
| PARAMID |
| PARAMETERNAME |
| START_DATE |
| LOAD_DATE |
- ← [[GALAXY.DEALER_DIM]]
| Column Name |
|---|
| DRM_SALES_CHANNEL_GEN07_DESC |
| SOURCE_DEALER_ID |
| START_DT_KEY |
| END_DT_KEY |

