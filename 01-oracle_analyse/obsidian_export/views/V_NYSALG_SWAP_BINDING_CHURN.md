# V_NYSALG_SWAP_BINDING_CHURN

**Schema:** `CCM` | **Type:** `View`

## Description
This view analyzes historical mobile postpaid subscriptions that originated as new sales ('NYSALG'). It combines data from mobile subscription history, household information, and subscription dimensions to provide details on customer age, subscription duration, binding status, and porting activities. A significant part of its function is to track and include information about product swaps associated with these new sales, capturing details like old and new products, sales type, dealer information, and associated revenue. The view appears to be designed for churn analysis or understanding the lifecycle and behavior of customers acquired through new mobile postpaid sales, excluding certain types of internal subscription changes.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MOBIL_SUBSCR_HIST]]
- ← [[GALAXY.SUBSCRIPTION_DIM]]
- ← [[CRM_ANALYSE.ADM_HOUSEHOLD_INFO_KURT_HIST]]
- ← [[ADHOC_BS.UK_1592_RES]]

