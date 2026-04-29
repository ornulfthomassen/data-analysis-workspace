# P_ADM_CUSTOMER_APP_USAGE_AGG

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Aggregates customer application usage data for a specified month (YYYYMM), performs source data validation, and then populates or updates a partition in the 'ADM_CUSTOMER_APP_USAGE_AGG' table using a temporary table and partition exchange.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| LAST_DATE_KEY |
| FIRST_DATE_KEY |
- ← [[CCDW_CUSTOMER_EVENT.CUSTOMER_EVENT_DETAIL]]
| Column Name |
|---|
| NUMBER_OF_EVENTS |
| EVENT_DATE_ID |
| SOURCE_SYSTEM_ID |
| EVENT_MEDIUM_ID |
| KURT_ID_EVENT |
| EVENT_TYPE_ID |
- ← [[CCDW_CUSTOMER_EVENT.EVENT_MEDIUM]]
| Column Name |
|---|
| EVENT_MEDIUM_ID |
| SOURCE_SYSTEM_ID |
| EVENT_MEDIUM_DESC |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |
- ← [[ADM_CUSTOMER_APP_USAGE_AGG]]

## Target Tables (Outputs)
- → [[TMP_CUSTOMER_APP_USAGE_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK |
| EVENT_MEDIUM_ID |
| NUMBER_OF_EVENT_DATES |
| NUMBER_OF_EVENT_TYPES |
| NUMBER_OF_EVENTS |
| FIRST_EVENT_DATE_KEY |
| LAST_EVENT_DATE_KEY |
| GET_INVOICE_EVENTS |
| DEFERE_INVOICE_EVENTS |
| EVENT_MEDIUM_DESC |
- → [[ADM_CUSTOMER_APP_USAGE_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK |
| EVENT_MEDIUM_ID |
| NUMBER_OF_EVENT_DATES |
| NUMBER_OF_EVENT_TYPES |
| NUMBER_OF_EVENTS |
| FIRST_EVENT_DATE_KEY |
| LAST_EVENT_DATE_KEY |
| GET_INVOICE_EVENTS |
| DEFERE_INVOICE_EVENTS |
| EVENT_MEDIUM_DESC |

