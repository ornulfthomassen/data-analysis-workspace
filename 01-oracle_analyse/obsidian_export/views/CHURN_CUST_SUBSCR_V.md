# CHURN_CUST_SUBSCR_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view combines detailed subscription information with demographic and financial data for both the 'owner' and 'user' associated with each subscription. It aims to provide a comprehensive dataset for analyzing customer churn by enriching subscription records with specific customer attributes for both the owning customer and the actual user of the subscription, including a classification of whether the owner and user are the same entity.

## Data Sources (Inputs)
- ← [[CLM_ADM.CHURN_SUBSCRIPTION_v]]
- ← [[CLM_ADM.CHURN_CUSTOMER_v]]

