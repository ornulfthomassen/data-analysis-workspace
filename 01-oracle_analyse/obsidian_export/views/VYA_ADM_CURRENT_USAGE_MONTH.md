# VYA_ADM_CURRENT_USAGE_MONTH

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies the most recent 'current usage month' (defined by a maximum period key less than 999912 from a mobile usage aggregation table) and retrieves its detailed period information along with data for the three preceding months from the ADM_MONTH_DIM table. It is intended for loading current usage month data into Mjøsa.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_CHAR |
| PERIOD_MONTH_KEY |
| PERIOD_MONTH_DATE |
| ANTALL_DAGER |
| PREV1_PERIOD_MONTH_CHAR |
| PREV1_PERIOD_MONTH_DATE |
| PREV1_ANTALL_DAGER |
| PREV2_PERIOD_MONTH_CHAR |
| PREV2_PERIOD_MONTH_DATE |
| PREV2_ANTALL_DAGER |
| PREV3_PERIOD_MONTH_CHAR |
| PREV3_PERIOD_MONTH_DATE |
| PREV3_ANTALL_DAGER |
- ← [[CLM_ADM.ADM_SUBS_USAGE_MOB_MONTH_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |

