# ADM_PRODUCT_ATTRIBUTE_VTMP

**Schema:** `CCM` | **Type:** `View`

## Description
This view, ADM_PRODUCT_ATTRIBUTE_VTMP, serves to consolidate, clean, and transform detailed product attribute information from various source fields. It performs extensive data type conversions (e.g., converting strings with units like 'KB', 'MB', 'GB' to numeric 'MB' values for included data and baud reduction quotas), standardizes fees (startup, monthly) and included services (minutes, SMS, MMS, data) into numeric formats, and derives product type hierarchy information. It also applies specific business rules and default values for certain product attributes based on product family, primary product flag, and product rank. The primary goal is to provide a comprehensive and consistent dataset of product characteristics for analytical purposes, excluding products from the 'Marius' source system.

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]

