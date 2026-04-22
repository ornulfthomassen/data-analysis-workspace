# FRAUD_DETECTION

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Identifies and lists detailed information about potential fraudulent purchasing activities related to mobile subscriptions and handsets. It flags customers who exhibit unusual purchasing patterns over the last 60 days, specifically those with a high number of total purchases relative to distinct main numbers (e.g., many purchases of few unique devices/subscriptions) or a high number of distinct main numbers, focusing on 'Voice' 'Subscription' products.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
- ← [[GALAXY.ORDER_LINE_PRODUCT_DIM_V]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[GALAXY.HANDSET_DIM_V]]
- ← [[GALAXY.CUSTOMER_DIM]]
- ← [[CLM_CCM.CCM_CUSTOMER_V]]
- ← [[GALAXY.SUBSCRIPTION_DIM_MV]]

