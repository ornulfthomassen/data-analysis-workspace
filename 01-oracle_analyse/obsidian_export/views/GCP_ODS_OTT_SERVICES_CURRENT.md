# GCP_ODS_OTT_SERVICES_CURRENT

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates aggregated Over-The-Top (OTT) service usage metrics for customers, including sums of usage over the last 7, 30, 60, and 90 days, corresponding KPIs (indicating if there was any usage in these periods), first/last service access timestamps, and total usage counts. It links raw service usage data to customer IDs and service descriptions, providing a consolidated view of current OTT service engagement per customer and service.

## Data Sources (Inputs)
- ← [[CCDW_USAGE.OTT_SERVICES_USAGE]]
- ← [[CCDW_USAGE.OTT_SERVICES]]
- ← [[CLM_CCM.CCM_USER_SERVICES_DIM]]
- ← [[ODS.CONNECT_ID_LINK]]

