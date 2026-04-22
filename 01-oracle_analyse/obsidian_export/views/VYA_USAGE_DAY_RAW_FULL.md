# VYA_USAGE_DAY_RAW_FULL

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides an aggregated daily snapshot of mobile subscription usage data. It calculates sums of various usage metrics such as net/gross amounts, discounts, volume (down/total), duration, roaming costs, cost of value, and number of events/CDRs. The data is grouped by day, month, owner/user customer, subscription, product, and various other dimensions like market area, call type, network operator, etc. It includes specific logic to handle 'twin' subscriptions, mask sensitive subscriber numbers (SUB_NUMBER) for main lines, and hash IMEI values. The view focuses on recent data, typically the current month and the previous three months, providing a consolidated and partially anonymized view of detailed mobile usage.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
- ← [[GALAXY.SUBSCR_USAGE_MOBILE_DAY_FACT_V]]
- ← [[CLM_ADM.ADM_MOB_SUBSCRIPTION_CORE]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]

