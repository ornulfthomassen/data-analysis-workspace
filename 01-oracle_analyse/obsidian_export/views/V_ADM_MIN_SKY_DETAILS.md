# V_ADM_MIN_SKY_DETAILS

**Schema:** `CCM` | **Type:** `View`

## Description
This view, V_ADM_MIN_SKY_DETAILS, provides a comprehensive monthly snapshot of 'Min Sky Service' activation and usage details for subscriptions and users. It combines core subscription information and the first activation event of the 'Min Sky Service' with historical monthly aggregated usage metrics. These metrics include data usage (GB/MB used), device connection/upload counts, file upload/download/delete activities, mobile device specifics (platforms, OS/client versions, auto-upload status), and various calculated monthly keys for tracking. The view is designed to consolidate these disparate data points for analytical purposes, offering insights into subscriber engagement and service utilization.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
- ← [[GALAXY.SUBSCRIPTION_DIM_MV]]
- ← [[COMOYO.COMOYO_SUB_GRANT_EVENTS]]
- ← [[CRM_ANALYSE.ADM_MIN_SKY_HIST]]
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
- ← [[CRM_ANALYSE.ADM_MONTH_DIM]]

