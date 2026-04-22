# VYA_ADM_SUBSCR_MASTER_HIST

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive historical overview of customer subscriptions. It consolidates various subscription attributes including unique identifiers, lifecycle details (such as original, previous, and past subscription IDs, start/end dates, and days between subscriptions), market area information, associated product groups, and port-in/port-out events. It also links subscription records to customer owner and user details from a customer mapping table and derives the subscription start reason, specifically identifying port-ins.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]

