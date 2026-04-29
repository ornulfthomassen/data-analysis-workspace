# GCP_ODS_OTT_SERVICES_CURRENT

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates Over-The-Top (OTT) service usage data, calculating access counts for various timeframes (last 7, 30, 60, 90 days), total access events, first/last access timestamps, and key performance indicators (KPIs) indicating recent activity. This usage information is then linked to customer IDs and standardized service names from dimension tables.

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
| SERVICE_NAME |
| SERVICE_OF_INTEREST |
- ← [[ODS.CONNECT_ID_LINK]]
| Column Name |
|---|
| CUSTOMER_ID |
| USER_ID |
| RANK_CONNECTION |
| ACTIVE_FLAG |

