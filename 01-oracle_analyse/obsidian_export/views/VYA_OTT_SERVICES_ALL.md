# VYA_OTT_SERVICES_ALL

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates OTT (Over-The-Top) service usage data by user and service, calculates usage metrics and KPIs over various timeframes (last 7, 30, 180 days, and total), and links the usage to customer and service dimension information. The output is intended for loading into a data mart or analytical system (referred to as 'Mjøsa'). It identifies the first and last access times for each user-service combination.

## Data Sources (Inputs)
- ← [[CCDW_USAGE.OTT_SERVICES_USAGE]]
| Column Name |
|---|
| SOURCE_USER_ID |
| FIRST_ACCESS_DTM |
| ACCESS_DTM |
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

