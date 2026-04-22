# BKV_SUBSCRIPTION_TEST

**Schema:** `CCM` | **Type:** `View`

## Description
Retrieves comprehensive details for active mobile subscriptions, including subscription attributes (e.g., main number, sub number, market area, IMEI, IMSI), associated product information (e.g., brand, market product group, payment type), and commercial customer data (e.g., customer name, company family, segment, employees). It specifically filters for mobile services with an end date in the future and resolves the primary subscription number for linked or hierarchical subscriptions.

## Data Sources (Inputs)
- ← [[galaxy.subscription_dim]]
- ← [[galaxy.subscr_detail_fact]]
- ← [[galaxy.product_dim]]
- ← [[galaxy.customer_dim]]

