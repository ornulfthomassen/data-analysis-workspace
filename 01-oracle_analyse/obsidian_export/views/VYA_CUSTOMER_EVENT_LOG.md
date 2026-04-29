# VYA_CUSTOMER_EVENT_LOG

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a consolidated log of recent customer events, enriching event details with event type and medium descriptions, and optionally mapping customer identifiers. It filters events to the last 30 days and handles varying timestamp formats for event dates.

## Data Sources (Inputs)
- ← [[CCDW_CUSTOMER_EVENT.CUSTOMER_EVENT_DETAIL]]
| Column Name |
|---|
| KURT_ID_EVENT |
| EVENT_DATE_ID |
| EVENT_TIME_OF_DAY_ID |
| CUSTOMER_EVENT_ID |
| EVENT_TYPE_ID |
| EVENT_MEDIUM_ID |
| SOURCE_SYSTEM_ID |
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
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |

