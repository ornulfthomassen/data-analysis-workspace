# KIM_PRODUCT_TREATMENT_DIM_VA

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates and enriches treatment-related information by incorporating details of up to six associated products and handset specifications. It joins the core 'KIM_TREATMENT_DIM' with 'PRODUCT_DIM_VA' multiple times to bring in product names and descriptions for `PRODUCT_KEY_1` through `PRODUCT_KEY_6`, and with 'HANDSET_DIM_VA' for handset marketing name and manufacturer. It serves as a comprehensive dimension for analytical purposes, providing a wide array of attributes for each treatment, including linked product and handset details.

## Data Sources (Inputs)
- ← [[KIM_TREATMENT_DIM]]
- ← [[PRODUCT_DIM_VA]]
- ← [[HANDSET_DIM_VA]]

