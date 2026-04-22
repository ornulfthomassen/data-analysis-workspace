# GCP_ADM_PRODUCT_ATTRIBUTE_HIST_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a monthly historical snapshot of product attributes by joining a month dimension with a historical product attribute table. It captures how product attributes (such as name, description, brand, payment type, technology, and various pricing details) evolve over time, making them accessible per specific month. The data is filtered to include months up to the end of the current year, effectively creating a time-aware dimension for product analysis.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_PRODUCT_ATTRIBUTE_HIST]]

