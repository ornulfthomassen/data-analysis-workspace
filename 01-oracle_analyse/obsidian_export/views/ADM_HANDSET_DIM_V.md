# ADM_HANDSET_DIM_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This Oracle SQL view, named ADM_HANDSET_DIM_V, serves as a dimension table for handset (mobile device) information. Its primary purpose is to standardize and consolidate various naming conventions for manufacturers and marketing names (models) of mobile devices. It achieves this through extensive CASE statements that map diverse raw input values to cleaner, more consistent categories. The view also retains the original source information as 'HAT_MANUFACTURER' and 'HAT_MARKETING_NAME' for traceability. This standardization is crucial for consistent reporting and analysis in a data warehousing environment.

## Data Sources (Inputs)
- ← [[CCDW.HANDSET_TYPE_EXT]]
- ← [[ADM_GSMA_MARKETING_NAME_DIM]]

