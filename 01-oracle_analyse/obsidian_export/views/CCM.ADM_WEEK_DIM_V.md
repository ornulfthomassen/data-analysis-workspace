# ADM_WEEK_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates daily date dimension data from the `GALAXY.DATE_DIM_MV` materialized view into weekly summaries. It calculates the first and last month, year, date key, and actual date for each week, along with the total number of days and working days within that week. The data is filtered to include weeks from January 2013 onwards and days up to two years in the future.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| YEAR_WEEK_NUMBER |
| RELATIVE_WEEK |
| YEAR_MONTH_NUMBER |
| RELATIVE_MONTH |
| YEAR |
| DATE_KEY |
| DAY |
| TYPE_OF_DAY |


