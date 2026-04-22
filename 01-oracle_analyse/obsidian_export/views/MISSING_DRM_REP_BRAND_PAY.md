# MISSING_DRM_REP_BRAND_PAY

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies and reports products that are associated with marketing treatments but have missing Data Relationship Management (DRM) attributes. It categorizes the type of missing DRM information (e.g., for reporting, brand, payment, or technology) and provides details of the affected products along with their linked treatment information. The primary purpose is to highlight data quality issues regarding product DRM metadata, especially for products involved in treatments, to ensure proper classification and reporting.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]
- ← [[GALAXY.PRODUCT_DIM]]

