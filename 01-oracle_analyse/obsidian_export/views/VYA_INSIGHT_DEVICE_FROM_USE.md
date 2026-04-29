# VYA_INSIGHT_DEVICE_FROM_USE

**Schema:** `CCM` | **Type:** `View`

## Description
The view `VYA_INSIGHT_DEVICE_FROM_USE` processes and consolidates unique IMEI (International Mobile Equipment Identity) device usage information. It extracts raw IMEI data, aggregates it to find the latest subscription and usage dates, and then generates various device-related identifiers such as HANDSET_KEY, IMEI_USE, IMEI_FULL, and IMEI_REST_SK. This device data is then enriched by joining with subscription and product mapping details from `CCDW.SUBSCRIPTION_MAPPING` and `ODS.SUBSCRIPTION_ODS_MOB` to include subscription keys, market area IDs, and product keys. The primary purpose is to load unique device records based on their usage for insightful analysis.

## Data Sources (Inputs)
- ← [[LIVE.EUREKA_IMEI]]
| Column Name |
|---|
| IMEI |
| SUBSCR_ID |
| RECORD_CHANGE_DATE |
| TERMINAL_USE_FIRST_DATE |
| TERMINAL_USE_LAST_DATE |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |
| SUBSCRIPTION_ID |
- ← [[ODS.SUBSCRIPTION_ODS_MOB]]
| Column Name |
|---|
| CUSTOMER_ROLE_ID |
| SUBSCRIPTION_ID |
| MARKET_AREA_ID |
| PRODUCT_OFFER_ID |

