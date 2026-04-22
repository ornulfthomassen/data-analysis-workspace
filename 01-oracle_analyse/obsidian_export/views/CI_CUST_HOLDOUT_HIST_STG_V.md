# CI_CUST_HOLDOUT_HIST_STG_V

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a staging view for customer holdout contact history, enriching it with customer and subscription master data. This view likely serves to aggregate and prepare historical data for customers assigned to control or 'holdout' groups within marketing campaigns or A/B tests, providing details on their activities, campaign participation, and related customer/subscription identifiers.

## Data Sources (Inputs)
- ← [[clm_rtdm.CLM_HOLDOUT_CONTACT_HIST_SDWN]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]

