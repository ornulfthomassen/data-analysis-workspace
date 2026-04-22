# VYA_ODS_OTT_HIST

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates historical Over-The-Top (OTT) service usage data. It calculates the number of distinct users ('NO_USER_ID') accessing specific OTT services on a given day, linked to a customer, along with the first access date for that service. It combines raw usage data with date dimensions, service dimensions, and customer linking information.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CCDW_USAGE.OTT_SERVICES_USAGE]]
- ← [[CCDW_USAGE.OTT_SERVICES]]
- ← [[CLM_CCM.CCM_USER_SERVICES_DIM]]
- ← [[ODS.CONNECT_ID_LINK]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]

