# VDO_SUBS_USAGE_DET_DAY

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides aggregated daily usage details for mobile subscriptions. It calculates total revenue amounts (net, gross, discount), data volume (down, total), call duration, roaming costs, and counts of events/CDRs. The data is grouped by various dimensions such as load date, event date, owner/user customer, subscription ID, sub number (with logic for distinguishing main/twin numbers), product, discount offer, subscription type/status, account, market area, destination/roaming country, call type, network operator, traffic type, agreement, device details (IMEI, IMSI, handset), pricing category, discount type, revenue category, CPA model, and content provider. It specifically focuses on mobile subscriptions with a `SUBSCRIPTION_TYPE_STATUS_KEY` of '3'.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_USAGE_MOBILE_DAY_FACT_V]]
- ← [[CLM_ADM.ADM_MOB_SUBSCRIPTION_CORE]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]

