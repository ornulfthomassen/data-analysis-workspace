# ADM33_APP_USAGE_AGG

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This Oracle SQL procedure aggregates customer event usage data from detailed transaction records and event medium descriptions. It calculates metrics such as event counts, unique event dates/types, and specific event categories (e.g., invoice events) for a specified period (range of months). The aggregated data is then inserted into two permanent summary tables: one at the subscription level (`ADM_KURT_SUBS_APP_USAGE_AGG`) and another at the application usage level (`ADM_KURT_APP_USAGE_AGG`). The procedure dynamically creates these target tables and their partitions if they do not exist, and manages their indexes and statistics.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
| SUBOBJECT_NAME |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[CCDW_CUSTOMER_EVENT.CUSTOMER_EVENT_DETAIL]]
| Column Name |
|---|
| EVENT_DATE_ID |
| SOURCE_SYSTEM_ID |
| EVENT_MEDIUM_ID |
| KURT_ID_EVENT |
| SUBSCRIPTION_ID |
| EVENT_TYPE_ID |
| NUMBER_OF_EVENTS |
- ← [[CCDW_CUSTOMER_EVENT.EVENT_MEDIUM]]
| Column Name |
|---|
| EVENT_MEDIUM_ID |
| EVENT_MEDIUM_DESC |
| SOURCE_SYSTEM_ID |

## Target Tables (Outputs)
- → [[ADM_KURT_SUBS_APP_USAGE_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| KURT_ID_EVENT |
| EVENT_MEDIUM_ID |
| SUBSCRIPTION_ID |
| NUMBER_OF_EVENT_DATES |
| NUMBER_OF_EVENT_TYPES |
| NUMBER_OF_EVENTS |
| FIRST_EVENT_DATE_KEY |
| LAST_EVENT_DATE_KEY |
| GET_INVOICE_EVENTS |
| DEFERE_INVOICE_EVENTS |
| EVENT_MEDIUM_DESC |
- → [[ADM_KURT_APP_USAGE_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| KURT_ID_EVENT |
| EVENT_MEDIUM_ID |
| NUMBER_OF_EVENT_DATES |
| NUMBER_OF_EVENT_TYPES |
| NUMBER_OF_EVENTS |
| FIRST_EVENT_DATE_KEY |
| LAST_EVENT_DATE_KEY |
| GET_INVOICE_EVENTS |
| DEFERE_INVOICE_EVENTS |
| EVENT_MEDIUM_DESC |

