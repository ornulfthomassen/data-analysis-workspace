# VYL_MONTH_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
This view serves as an enhanced month dimension, providing detailed temporal attributes for a given month, including its key, character representation (e.g., 'YYYYMM'), first and last dates, total days, and working days. Crucially, it extends this information to include attributes for the *next* month and the *six preceding* months (PREV1 through PREV6). This makes it highly useful for time-series analysis, comparisons across months, and reporting that requires looking at past or future periods relative to a current month.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]

