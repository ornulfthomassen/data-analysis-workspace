# VYA_ODS_OTT_HIST_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates historical app (OTT service) usage data by month, customer, and service, providing metrics such as first and last usage dates, total days of usage, and the number of unique user IDs. This aggregated data is intended for loading into a data warehouse or reporting system ('Mjøsa').

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[COMOYO.USER_SERVICES_SERVICE_SCD]]
- ← [[CLM_CCM.CCM_USER_SERVICES_DIM]]
- ← [[ODS.CONNECT_ID_LINK]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]

