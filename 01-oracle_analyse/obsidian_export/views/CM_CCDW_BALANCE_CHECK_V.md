# CM_CCDW_BALANCE_CHECK_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view performs a data reconciliation and balance check between the CM (Customer Management) system and the CCDW (Customer Centric Data Warehouse) system for subscription data. It identifies and categorizes discrepancies in subscription status, specifically highlighting subscriptions that are active in one system but inactive, unknown, or not correctly reflected in the other. The view aims to detect and report issues where subscriptions in CM are not in sync with their representation in CCDW, based on specific date criteria (typically before the last CCDW load time).

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[CM.SUBSCRIPTION]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CM.CUSTOMER]]

