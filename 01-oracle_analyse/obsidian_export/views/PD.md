# PD

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `PD`, provides a comprehensive and highly categorized list of product attributes, primarily by joining product dimension data with administrative product attributes. Its main purpose is to standardize, classify, and enrich product information from various source systems (KAS, FKM, deFakto, Pacman). It calculates derived product categories (e.g., PRODUCT_REPORT_LEVEL1 to PRODUCT_REPORT_FMC) based on various attributes like product description, business area, technology, and payment type. It also includes details about included quantities (minutes, SMS, MB) and pricing, along with saleability flags. The extensive use of `CASE` statements indicates a complex business logic for product classification and reporting, suitable for analytical purposes.

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_ADM.ADM_PRODUCT_ATTRIBUTE_V]]

