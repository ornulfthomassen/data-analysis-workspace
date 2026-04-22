# CHURN_CUSTOMER_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Provides a historical snapshot of customer attributes and subscription metrics relevant for churn analysis. It filters data for the last 24 months, ending with the previous calendar month, including customer demographics, revenue, product subscription counts (fiber, mobile broadband, mobile postpaid, etc.), and a customer life stage segment. The view renames several columns for clarity and specific reporting needs.

## Data Sources (Inputs)
- ← [[CLM_ADM.CHURN_ADM_CUSTOMER]]

