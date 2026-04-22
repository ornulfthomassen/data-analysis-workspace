# V_MPR_TOP_UP_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates top-up (recharge) data by subscription and month, categorizing the number and monetary amount of top-ups by various payment channels such as payment card, mobile purchase, ATM, hotline activation, and scratch card. It also calculates total top-ups and total amounts for each subscription and period.

## Data Sources (Inputs)
- ← [[AGR.AG_EDR]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]

