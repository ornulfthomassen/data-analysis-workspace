# ADM_WEEK_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates daily data from the `DATE_DIM_MV` into weekly summaries. For each week, it calculates various temporal boundaries such as the first and last year-month numbers, date keys, and actual dates. It also computes the total number of days and working days within each week. Additionally, it provides a 'relative week' and 'relative month' number, adjusted by a constant offset derived from a specific reference date (2013-01-01). The data is filtered to include dates from January 2013 onwards, up to approximately two years into the future from the current date.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]

