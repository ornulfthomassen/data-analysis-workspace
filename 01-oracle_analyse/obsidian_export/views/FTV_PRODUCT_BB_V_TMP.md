# FTV_PRODUCT_BB_V_TMP

**Schema:** `CCM` | **Type:** `View`

## Description
The view FTV_PRODUCT_BB_V_TMP standardizes, categorizes, and enriches product information, primarily focusing on broadband (BB) and TV services. It derives various business-specific attributes such as subscription type, dwelling unit type, product speed, technology, value chain, product priority, and source tags based on complex business rules and data from multiple source systems. It consolidates product data from a core product dimension table and specific product details from the KAS system, filtering for relevant and active products.

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[KAS.PRODUKT]]

