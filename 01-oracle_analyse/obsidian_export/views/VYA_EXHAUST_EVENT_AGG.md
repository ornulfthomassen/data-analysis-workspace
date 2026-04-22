# VYA_EXHAUST_EVENT_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates 'exhaust events' (data usage reaching limits, leading to early exhaustion or speed reduction) from customer activity logs on a monthly basis. For each subscription and month, it calculates the count, first occurrence date, and last occurrence date of these events, distinguishing between notifications sent to the owner's contact number and the main number. It then enriches this aggregated event data with product family name and product name information.

## Data Sources (Inputs)
- ← [[CUSTOMERLOG.ACTIVITY_LOG]]
- ← [[CM.SUBSCRIPTION]]
- ← [[CUSTOMERLOG.ACTIVITY_MEDIUM]]
- ← [[CUSTOMERLOG.ACTIVITY_STATUS]]
- ← [[CUSTOMERLOG.ACTIVITY_EVENT]]
- ← [[CUSTOMERLOG.ACTIVITY_DESCRIPTION]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
- ← [[PD]]

