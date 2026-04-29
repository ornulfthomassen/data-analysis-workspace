# VYL_MONTH_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
This view, 'VYL_MONTH_DIM', serves as a comprehensive month dimension table. It consolidates monthly attributes such as period keys, first/last dates, total days, and working days for the current month, the immediate next month, and six preceding months. It enriches the numerical month dimension data with character-based month descriptions for these periods, making it suitable for time-series analysis and reporting that requires historical and future month context.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| RELATIVE_MONTH |
| PERIOD_MONTH_KEY |
| FIRST_DATE_KEY |
| LAST_DATE_KEY |
| FIRST_DATE |
| LAST_DATE |
| ANTALL_DAGER |
| ANTALL_ARBEIDSDAGER |
| NEXT_PERIOD_MONTH_KEY |
| NEXT_FIRST_DATE_KEY |
| NEXT_LAST_DATE_KEY |
| NEXT_FIRST_DATE |
| NEXT_LAST_DATE |
| NEXT_ANTALL_DAGER |
| NEXT_ANTALL_ARBEIDSDAGER |
| PREV1_PERIOD_MONTH_KEY |
| PREV1_FIRST_DATE_KEY |
| PREV1_LAST_DATE_KEY |
| PREV1_FIRST_DATE |
| PREV1_LAST_DATE |
| PREV1_ANTALL_DAGER |
| PREV1_ANTALL_ARBEIDSDAGER |
| PREV2_PERIOD_MONTH_KEY |
| PREV2_FIRST_DATE_KEY |
| PREV2_LAST_DATE_KEY |
| PREV2_FIRST_DATE |
| PREV2_LAST_DATE |
| PREV2_ANTALL_DAGER |
| PREV2_ANTALL_ARBEIDSDAGER |
| PREV3_PERIOD_MONTH_KEY |
| PREV3_FIRST_DATE_KEY |
| PREV3_LAST_DATE_KEY |
| PREV3_FIRST_DATE |
| PREV3_LAST_DATE |
| PREV3_ANTALL_DAGER |
| PREV3_ANTALL_ARBEIDSDAGER |
| PREV4_PERIOD_MONTH_KEY |
| PREV4_FIRST_DATE_KEY |
| PREV4_LAST_DATE_KEY |
| PREV4_FIRST_DATE |
| PREV4_LAST_DATE |
| PREV4_ANTALL_DAGER |
| PREV4_ANTALL_ARBEIDSDAGER |
| PREV5_PERIOD_MONTH_KEY |
| PREV5_FIRST_DATE_KEY |
| PREV5_LAST_DATE_KEY |
| PREV5_FIRST_DATE |
| PREV5_LAST_DATE |
| PREV5_ANTALL_DAGER |
| PREV5_ANTALL_ARBEIDSDAGER |
| PREV6_PERIOD_MONTH_KEY |
| PREV6_FIRST_DATE_KEY |
| PREV6_LAST_DATE_KEY |
| PREV6_FIRST_DATE |
| PREV6_LAST_DATE |
| PREV6_ANTALL_DAGER |
| PREV6_ANTALL_ARBEIDSDAGER |
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY_CHAR |
| PERIOD_MONTH_KEY |

