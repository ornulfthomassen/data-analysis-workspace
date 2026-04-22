# GCP_INSIGHT_CONSUMPTION

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and calculates various subscription-based consumption metrics, revenue details, and rollover data, primarily for mobile services (data, calls, SMS, MMS) over different time periods (current, 30-day, and several previous months). It provides insights into customer usage patterns, data consumption types (e.g., net, campaign, roaming, freedom plans), revenue associated with subscriptions, and twin-SIM usage, likely for business intelligence and analytics related to telecommunication services.

## Data Sources (Inputs)
- ← [[CCM.VYA_ODS_SUBSCRIPTION]]
- ← [[CCM.VYA_ADM_CURRENT_USAGE_MONTH]]
- ← [[CCM.VYA_MONTH_DIM]]
- ← [[CCM.VYA_CCM_SUBSCR_MOB_USAGE]]
- ← [[CCM.VYA_CCM_ROLLOVER]]
- ← [[CCM.VYA_ADM_SUBS_USAGE_MONTH_CURR]]
- ← [[CCM.VYA_ADM_SUBS_USAGE_MONTH_D30]]
- ← [[CCM.VYA_ADM_SUBS_USAGE_MONTH_AGG]]
- ← [[CCM.VYA_ADM_SUBS_REVENUE]]

