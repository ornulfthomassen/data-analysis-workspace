# FTV_PRODUCT_BB_V_DEV

**Schema:** `CCM` | **Type:** `View`

## Description
Consolidates and categorizes fixed broadband (BB) and television (TV) product information from various source systems (KAS, deFakto, Pacman). It transforms raw product data by deriving new attributes such as SUBSCRIPTION_TYPE, DWELLING_UNIT_TYPE, TECHNOLOGY, VALUECHAIN, and PRODUCT_PRIORITY, and standardizes speed-related metrics. This view aims to provide a unified, enriched, and classified product dimension for reporting and analytical purposes.

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[DUAL]]

