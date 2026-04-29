# VYA_ODS_CURRENT_OTT

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates OTT (Over-The-Top) service usage data by customer and service name, providing metrics such as total usage, usage within the last 30, 60, and 90 days, first/last service access timestamps, and a KPI indicating recent service activity.

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
| SERVICE_NAME |
| SERVICE_CD |
| SERVICE_OF_INTEREST |
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
| CUSTOMER_SK |
| KURT_ID |

