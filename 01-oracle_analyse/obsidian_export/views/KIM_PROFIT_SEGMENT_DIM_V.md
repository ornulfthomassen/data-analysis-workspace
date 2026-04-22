# KIM_PROFIT_SEGMENT_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view serves as a dimension for customer profitability segments. It combines segment details with information about their associated models, specifically filtering for models named 'Kundelønnsomhet' (Customer profitability). It provides a consolidated view of segment ID, name, criteria, comment, and the ID, name, and description of the relevant profitability model.

## Data Sources (Inputs)
- ← [[CCDW_SEGMENT.SEGMENT]]
- ← [[CCDW_SEGMENT.MODEL]]

