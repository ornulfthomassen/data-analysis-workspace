# V_DATE_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `V_DATE_DIM`, serves as a comprehensive date dimension table, providing a wide array of date-related attributes such as day, week, month, quarter, and year details, along with various time-relative flags (e.g., current week, last month, year-to-date). It acts as a wrapper or simplified access point to an underlying materialized view, making date-based analytics easier for applications or users within the `CRM_ANALYSE` schema.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]

