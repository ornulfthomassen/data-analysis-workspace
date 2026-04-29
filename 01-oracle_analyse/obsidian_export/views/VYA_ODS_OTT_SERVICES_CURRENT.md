# VYA_ODS_OTT_SERVICES_CURRENT

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates Over-The-Top (OTT) service usage statistics, calculating first and last access timestamps, total accesses, and usage counts over recent periods (7, 30, 60, and 90 days). It then links these aggregated usage metrics with customer and service dimension information, deriving Key Performance Indicators (KPIs) for recent service activity.

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

