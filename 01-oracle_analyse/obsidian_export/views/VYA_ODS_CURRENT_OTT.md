# VYA_ODS_CURRENT_OTT

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates aggregated Over-The-Top (OTT) service usage metrics (total access counts within the last 30, 60, 90 days, total overall access count, first and last access timestamps, and key performance indicators for recent activity) by customer and service name. It links raw OTT service usage data to customer master data via user IDs and service dimensions, providing a customer-centric view of OTT service engagement.

## Data Sources (Inputs)
- ← [[CCDW_USAGE.OTT_SERVICES_USAGE]]
- ← [[CCDW_USAGE.OTT_SERVICES]]
- ← [[CLM_CCM.CCM_USER_SERVICES_DIM]]
- ← [[ODS.CONNECT_ID_LINK]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]

