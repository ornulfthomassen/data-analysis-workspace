# V_GALAXY_DATE_DIM_MV

**Schema:** `CCM` | **Type:** `View`

## Description
This view serves as a direct alias or a wrapper for the `galaxy.DATE_DIM_MV` object. It exposes all columns from the underlying `DATE_DIM_MV`, which is presumably a comprehensive date dimension table or materialized view containing various date attributes (e.g., day, month, year, quarter) and pre-calculated time-period flags (e.g., current week/month/year, last 12 months, year-to-date). Its primary purpose is to make these date dimension attributes available under a specific schema (`CRM_ANALYSE`) without any additional transformations or filtering.

## Data Sources (Inputs)
- ← [[galaxy.DATE_DIM_MV]]

