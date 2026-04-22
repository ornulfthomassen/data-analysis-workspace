# VYA_OTT_SERVICES_ALL

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates and calculates Over-The-Top (OTT) service usage statistics per user and service over various time periods (last 7, 30, 180 days, and total). It derives key performance indicators (KPIs) for recent usage and links the usage data to customer information, transforming user IDs and providing customer identifiers. The overall purpose is to load application usage data.

## Data Sources (Inputs)
- ← [[CCDW_USAGE.OTT_SERVICES_USAGE]]
- ← [[CCDW_USAGE.OTT_SERVICES]]
- ← [[CLM_CCM.CCM_USER_SERVICES_DIM]]
- ← [[ODS.CONNECT_ID_LINK]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]

