# CHURN_SUBSCR_PROD_RAW_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view, 'CHURN_SUBSCR_PROD_RAW_V', extracts specific subscription product details including period month key, subscription key, product start/end dates, market product identifier, product name, description, and source product ID. Its primary purpose is to provide a filtered dataset of recent subscription product data, limited to the last 25 full months up to and including the current month (based on 'period_month'), likely for churn analysis or reporting.

## Data Sources (Inputs)
- ← [[ccm.vya_churn_wide_subscr_products]]

