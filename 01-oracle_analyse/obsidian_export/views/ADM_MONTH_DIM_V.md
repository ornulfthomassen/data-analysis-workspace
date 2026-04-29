# ADM_MONTH_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a monthly dimension view by aggregating data from the `DATE_DIM_MV` table, providing month-level summaries such as period keys, month names, relative month, first and last dates, total days, and total working days. The data is filtered for specific year-month numbers and relative months.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| YEAR_MONTH_NUMBER |
| MONTH_NAME |
| RELATIVE_MONTH |
| DATE_KEY |
| DAY |
| TYPE_OF_DAY |

