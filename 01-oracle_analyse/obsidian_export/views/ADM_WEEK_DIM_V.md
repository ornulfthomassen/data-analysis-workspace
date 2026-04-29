# ADM_WEEK_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates weekly information from a date dimension materialized view (`GALAXY.DATE_DIM_MV`). It calculates various date-related metrics for each week, such as the first and last year-month numbers, relative month numbers, years, and date keys. It also provides the first and last actual dates, the total number of days, and the sum of 'working days' within each week. The data is filtered to include weeks from January 2013 onwards and up to approximately two years into the future from the current date.

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

