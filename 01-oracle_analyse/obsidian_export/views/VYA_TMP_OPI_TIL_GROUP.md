# VYA_TMP_OPI_TIL_GROUP

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates event data for a specific source system (ID 67), event type (ID 226337067), and event medium ('Mitt Telenor'), focusing on the previous month. It calculates the number of days with events, total unique sessions (based on KURT_ID_EVENT), unique users for the month (also based on KURT_ID_EVENT), and unique users per day (based on a combination of event date and KURT_ID_EVENT). The primary purpose is to provide monthly aggregated statistics related to user activity or sessions for a particular application or service.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
- ← [[CCDW_CUSTOMER_EVENT.CUSTOMER_EVENT_DETAIL]]
- ← [[CCDW_CUSTOMER_EVENT.EVENT_MEDIUM]]

