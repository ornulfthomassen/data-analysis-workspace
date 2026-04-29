# VYA_ODS_OTT_HIST_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates historical Over-The-Top (OTT) app usage data, such as streaming services, by month, customer, and service. It calculates the minimum and maximum usage dates, the first usage date of a service, the total number of days a service was used, and the count of unique user IDs for each period, customer, and service combination. The view links app usage to customer information through user IDs and customer mappings.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_CHAR |
| PERIOD_MONTH_DATE |
| LAST_DATE |
| FIRST_DATE |
- ← [[COMOYO.USER_SERVICES_SERVICE_SCD]]
| Column Name |
|---|
| END_DATE |
| USER_ID |
| SERVICE_NAME |
| SERVICE_FIRST_DATE |
- ← [[CLM_CCM.CCM_USER_SERVICES_DIM]]
| Column Name |
|---|
| SERVICE_CD |
| SERVICE_OF_INTEREST |
| SERVICE_NAME |
- ← [[ODS.CONNECT_ID_LINK]]
| Column Name |
|---|
| USER_ID |
| RANK_CONNECTION |
| ACTIVE_FLAG |
| CUSTOMER_ID |
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |

