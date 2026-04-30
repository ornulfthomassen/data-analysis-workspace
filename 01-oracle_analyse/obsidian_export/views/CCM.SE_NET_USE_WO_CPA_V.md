# SE_NET_USE_WO_CPA_V

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates aggregated net usage metrics, distinguishing between CPA (Cost Per Acquisition) and non-CPA business models, for specific subscription types, grouped by period month and subscription.

## Data Sources (Inputs)
- ← [[GALAXY.TRAFFIC_MONTH_FACT_V]]
| Column Name |
|---|
| PERIODE_MONTH_KEY |
| SUBSCRIPTION_KEY |
| CPA_BUSINESS_MODEL_KEY |
| TRAFFIC_NET_AMOUNT |
| TRAFFIC_NET_DISCOUNT_AMOUNT |
| SUBSCR_TYPE_STATUS_KEY |


