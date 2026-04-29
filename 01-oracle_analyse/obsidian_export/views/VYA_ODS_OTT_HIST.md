# VYA_ODS_OTT_HIST

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates historical Over-The-Top (OTT) service usage data by day, customer, and service. It links raw usage records with service dimensions and customer identifiers to provide a count of unique users for specific services and dates, primarily intended for 'APP-usage' reporting.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| DATE_KEY |
- ← [[CCDW_USAGE.OTT_SERVICES_USAGE]]
| Column Name |
|---|
| SOURCE_USER_ID |
| FIRST_ACCESS_DTM |
| ACCESS_DT_ID |
| OTT_SERVICE_ID |
- ← [[CCDW_USAGE.OTT_SERVICES]]
| Column Name |
|---|
| SOURCE_SERVICE_NAME |
| OTT_SERVICE_ID |
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

