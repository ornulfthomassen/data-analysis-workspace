# VYAMN_CUSTOMER_EVENT_LOG

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a unified log of customer events, enriching event details with customer mapping information (for event, owner, payer, and user), event types, and event medium descriptions. The view filters for recent event data, typically from the last two years.

## Data Sources (Inputs)
- ← [[CCDW_CUSTOMER_EVENT.CUSTOMER_EVENT_DETAIL]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MARKET_AREA_ID |
| EVENT_DATE_ID |
| EVENT_TIME_OF_DAY_ID |
| CUSTOMER_EVENT_ID |
| EVENT_TYPE_ID |
| EVENT_MEDIUM_ID |
| KURT_ID_EVENT |
| KURT_ID_OWNER |
| KURT_ID_PAYER |
| KURT_ID_USER |
- ← [[CCDW_CUSTOMER_EVENT.EVENT_TYPE]]
| Column Name |
|---|
| EVENT_TYPE_ID |
| SOURCE_EVENT_TYPE_ID1 |
| SOURCE_EVENT_TYPE_ID2 |
| SOURCE_EVENT_TYPE_ID3 |
| SOURCE_EVENT_TYPE_ID4 |
| EVENT_TYPE_DESC1 |
| EVENT_TYPE_DESC2 |
| EVENT_TYPE_DESC3 |
| EVENT_TYPE_DESC4 |
- ← [[CCDW_CUSTOMER_EVENT.EVENT_MEDIUM]]
| Column Name |
|---|
| EVENT_MEDIUM_ID |
| EVENT_MEDIUM_DESC |
- ← [[CCDW.CUSTOMER_MAPPING]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |

