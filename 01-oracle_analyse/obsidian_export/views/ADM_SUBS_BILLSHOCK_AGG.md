# ADM_SUBS_BILLSHOCK_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates mobile subscription bill shock and related usage metrics (like 'NOK' and 'ANTALL_TWIN') over different historical periods. It provides data points for the current month, the two previous months, and cumulative sums for the last 6 and 12 months. The 'bill shock' is specifically defined by 'NOK' exceeding 398.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_BILL_SHOCK]]

