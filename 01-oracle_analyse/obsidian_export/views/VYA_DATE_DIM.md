# VYA_DATE_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a comprehensive date dimension view, `VYA_DATE_DIM`, for analytics and reporting purposes. It selects a wide array of date-related attributes (e.g., day, week, month, quarter, year numbers and names, relative periods like current, last, next week/month/year, and year-to-date calculations) from an existing date dimension materialized view. It also performs minor data type casting and calculates a new `YEAR_OF_WEEK` column.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]

