# KIM_DATE_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a comprehensive date dimension view by selecting various date attributes from the `GALAXY.DATE_DIM_MV` materialized view and augmenting them with calculated relative week and month values based on the current system date.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DATE_KEY |
| DAY |
| DAY_OF_WEEK |
| DAY_OF_WEEK_SHORT |
| TYPE_OF_DAY |
| WEEK_ENDING |
| WEEK_NUMBER |
| WEEK_YEAR_NUMBER |
| YEAR_WEEK_NUMBER |
| MONTH_NAME |
| MONTH_SHORT_NAME |
| MONTH_NUMBER |
| MONTH_YEAR_NUMBER |
| YEAR_MONTH_NUMBER |
| QUARTER_NAME |
| QUARTER_NUMBER |
| QUARTER_YEAR |
| QUARTER_YEAR_NUMBER |
| YEAR_QUARTER_NUMBER |
| YEAR |
| CURRENT_WEEK |
| CURRENT_MONTH |
| CURRENT_YEAR |
| LAST_4_WEEKS |
| YEAR_TO_DATE |
| LAST_MONTH |
| LAST_WEEK |

