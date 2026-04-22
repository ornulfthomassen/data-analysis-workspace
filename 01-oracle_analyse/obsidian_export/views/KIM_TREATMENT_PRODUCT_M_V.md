# KIM_TREATMENT_PRODUCT_M_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive and categorized representation of CRM treatments. It consolidates data from various treatment-related tables, enriches it with product configuration details, and derives business-friendly classifications for KPI type, action category, action category type, and offer category. The primary purpose is to offer a flattened, analytical view of treatments and their associated product information, often for reporting or data warehousing dimensions.

## Data Sources (Inputs)
- ← [[CLM_CDM.CI_TREATMENT]]
- ← [[CLM_CDM.CI_TREATMENT_EXT]]
- ← [[CLM_CDM.CI_TREATMENT_CHAR_UDF]]
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]

