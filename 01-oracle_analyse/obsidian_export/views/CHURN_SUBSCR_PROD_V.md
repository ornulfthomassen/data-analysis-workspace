# CHURN_SUBSCR_PROD_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view standardizes and prepares detailed information for a specific set of subscription products within monthly periods. It calculates the number of days each product was active within a given month and flags whether the product started or ended in that month. Additionally, it performs extensive cleaning and standardization of product names and market categories, making the data suitable for churn analysis or other subscription product lifecycle insights.

## Data Sources (Inputs)
- ← [[CLM_ADM.CHURN_SUBSCR_PROD_RAW_V]]

