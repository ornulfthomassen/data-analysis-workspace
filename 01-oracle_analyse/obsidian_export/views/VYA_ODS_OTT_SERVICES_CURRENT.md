# VYA_ODS_OTT_SERVICES_CURRENT

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates Over-The-Top (OTT) service usage data, calculating access counts for various recent periods (last 7, 30, 60, 90 days), total access counts, and first/last access timestamps. It also derives Key Performance Indicators (KPIs) indicating whether a service was accessed within these periods. The usage data, initially tracked by user ID and service name, is then linked to a customer identifier (CUSTOMER_SK) using customer mapping and service dimension tables. Essentially, it provides a customer-centric overview of OTT service engagement and activity.

## Data Sources (Inputs)
- ← [[CCDW_USAGE.OTT_SERVICES_USAGE]]
- ← [[CCDW_USAGE.OTT_SERVICES]]
- ← [[CLM_CCM.CCM_USER_SERVICES_DIM]]
- ← [[ODS.CONNECT_ID_LINK]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]

