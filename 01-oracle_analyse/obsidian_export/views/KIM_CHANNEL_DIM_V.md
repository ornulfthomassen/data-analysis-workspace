# KIM_CHANNEL_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a standardized and cleaned view of channel dimension data. It handles NULL values by replacing them with '-1' (as a string literal) and enforces specific VARCHAR2 lengths for several columns. It also renames the 'CHANNEL_COMMON_NM' column to 'CHANNEL' for consistency or simplification.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CHANNEL_DIM]]

