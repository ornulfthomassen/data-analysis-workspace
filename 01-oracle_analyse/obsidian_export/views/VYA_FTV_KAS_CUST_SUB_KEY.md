# VYA_FTV_KAS_CUST_SUB_KEY

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates and pivots singular 'Bredbånd' (broadband) and 'TV' subscription details for customers originating from the 'KAS' source system. For each customer, it extracts the `SUBSCRIPTION_KEY` and `KAS_ABONNENT_NR` for both 'Bredbånd' and 'TV' categories, provided the customer has exactly one distinct primary subscription in each respective category. These details are then presented in dedicated columns prefixed with 'BB_' for broadband and 'TV_' for television subscriptions. The view primarily focuses on customers with a unique, primary subscription in these categories.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
- ← [[GALAXY.SUBSCRIPTION_DIM]]

