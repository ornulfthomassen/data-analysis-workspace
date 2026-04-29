# P_ADM_CUST_SUBS_APP_USAGE_AGG

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Aggregates customer subscription application usage data for a specified month (P_YYYYMM), performs data quality and completeness checks on source tables, creates a temporary staging table with the aggregated data, and then uses partition exchange to load this data into the corresponding partition of a permanent, partitioned target table 'ADM_CUST_SUBS_APP_USAGE_AGG'. It also handles the creation of new partitions if they don't exist and gathers table statistics.

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
| EVENT_DATE_ID |
| SOURCE_SYSTEM_ID |
| EVENT_MEDIUM_ID |
| NUMBER_OF_EVENTS |
| KURT_ID_EVENT |
| SUBSCRIPTION_ID |
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

## Target Tables (Outputs)
- → [[TMP_CUST_SUBS_APP_USAGE_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK |
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
- → [[ADM_CUST_SUBS_APP_USAGE_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK |
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
- → [[CRM_ANALYSE.ADM_LOAD_HISTORY]]
| Column Name |
|---|
| TABLE_NAME |
| PERIOD_MONTH |
| STATUS |
| MESSAGE |

