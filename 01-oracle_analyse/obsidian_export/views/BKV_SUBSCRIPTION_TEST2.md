# BKV_SUBSCRIPTION_TEST2

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a consolidated and detailed perspective on active or recently active subscriptions. It combines subscription details with associated product information and customer attributes. Key features include identifying a 'primary subscription number' for child subscriptions, handling specific customer segment values, and filtering data to focus on relevant source systems and current/recent primary product end dates. The view aims to offer a comprehensive, flattened record for each unique combination of subscription, product, and customer characteristics.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
- ← [[GALAXY.SUBSCRIPTION_DIM]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.CUSTOMER_DIM]]

