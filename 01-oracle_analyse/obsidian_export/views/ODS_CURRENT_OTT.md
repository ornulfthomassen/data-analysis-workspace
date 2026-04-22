# ODS_CURRENT_OTT

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates 'Over-The-Top' (OTT) service usage data by customer and service. For each customer (identified by `CUSTOMER_SK`) and specific service (`SERVICE_NAME`), it determines the earliest start date, the latest end date, and counts the number of associated user IDs (`NO_USER_ID`). It filters for current records, services marked as 'of interest', and primary/active customer connections.

## Data Sources (Inputs)
- ← [[COMOYO.USER_SERVICES_SERVICE_SCD]]
- ← [[CLM_CCM.CCM_SERVICES_DIM]]
- ← [[ODS.CONNECT_ID_LINK]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]

