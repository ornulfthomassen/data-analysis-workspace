# VYA_EXHAUST_EVENT_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates data usage exhaust events (e.g., 'early exhaust', 'exhausted, speed reduced') from customer activity logs. It categorizes these events by type (early exhaust vs. exhausted) and notification recipient (owner contact number vs. main number). For each month and subscription, it counts the occurrences and identifies the first and last dates of these events. Finally, it enriches the aggregated event data with product family and product name information, primarily for analysis and generating sales tips.

## Data Sources (Inputs)
- ← [[CUSTOMERLOG.ACTIVITY_LOG]]
| Column Name |
|---|
| INFO_REG_DATE |
| ACT_LOG_ID |
| SUBSCR_ID |
| ACT_MEDIUM_ID |
| ACT_STATUS_ID |
| ACT_EVENT_LEVEL1_ID |
| ACT_EVENT_LEVEL2_ID |
| ACT_EVENT_LEVEL3_ID |
| DESCRIPTION_ID |
| EXT_DATA_ID |
- ← [[CM.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCR_ID |
| DIRECTORY_NUMBER_ID |
- ← [[CUSTOMERLOG.ACTIVITY_MEDIUM]]
| Column Name |
|---|
| ACT_MEDIUM_ID |
- ← [[CUSTOMERLOG.ACTIVITY_STATUS]]
| Column Name |
|---|
| ACT_STATUS_ID |
| ACT_STATUS_DESCR |
- ← [[CUSTOMERLOG.ACTIVITY_EVENT]]
| Column Name |
|---|
| ACT_EVENT_ID |
- ← [[CUSTOMERLOG.ACTIVITY_DESCRIPTION]]
| Column Name |
|---|
| DESCRIPTION_ID |
| DESCRIPTION_1 |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |
| SUBSCRIPTION_ID |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| PRODUCT_OFFER_ID |
- ← [[PD]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_FAMILY_NAME |
| PRODUCT_NAME |

