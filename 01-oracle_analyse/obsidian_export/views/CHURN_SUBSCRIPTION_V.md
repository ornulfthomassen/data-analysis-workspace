# CHURN_SUBSCRIPTION_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view, 'CHURN_SUBSCRIPTION_V', extracts and transforms subscription-related data, specifically for the 'MPP' product group. It calculates a 'revenue_fee_ratio' and filters records to include a rolling 25-month period (current month and the 24 months preceding the previous month). The selected columns suggest its purpose is to provide a comprehensive dataset for analyzing churn behavior, subscription performance, and customer metrics related to these subscriptions.

## Data Sources (Inputs)
- ← [[CLM_ADM.CHURN_ADM_SUBSCRIPTION]]

