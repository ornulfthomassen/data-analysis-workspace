# CURRENT_STOCK_POID_QA

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and consolidates the current active count (referred to as 'balance' or 'stock') of specific consumer subscription and voice products from various source systems. It provides a multi-source inventory, showing the product name, product offer ID (POID), the count from that source, and an indicator ('KILDE') of which source system the data originated from. The view specifically focuses on consumer products categorized as 'Abonnement' (Subscription) and 'Tale' (Voice) that are marked as primary products.

## Data Sources (Inputs)
- ← [[CM.REL_NUMBER]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CM.SUBSCRIPTION]]
- ← [[CM.SUBSCRIPTION_OFFER_INCENTIVE]]
- ← [[ODS.SUBSCRIPTION_ODS_MOB]]
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[CCDW.SUBSCRIBED_PRODUCT]]

