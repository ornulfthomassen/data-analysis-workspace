# DATE_DIM_VA

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a comprehensive date dimension for analytical purposes, standardizing date-related attributes and flags (e.g., day, month, quarter, year, current/last period indicators, YTD) from an underlying materialized view. It handles potential null values by defaulting them to -1 and explicitly casts various date attributes to VARCHAR2.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]

