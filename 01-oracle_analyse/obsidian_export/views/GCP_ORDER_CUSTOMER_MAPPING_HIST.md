# GCP_ORDER_CUSTOMER_MAPPING_HIST

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a historical mapping of order, subscription, and agreement details to owner and user customer information. It selects data from a source table, applying data type conversions (e.g., VARCHAR2 to NUMBER) and trimming whitespace for various identifiers and keys, making the data available in a structured format.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_ORDER_CUSTOMER_MAPPING_HIST]]

