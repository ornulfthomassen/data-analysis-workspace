# V_MPR_TOP_UP_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates monthly top-up statistics per subscription, categorizing top-ups by channel (e.g., payment card, mobile purchase, ATM, hotline activation, scratch card) and providing counts and amounts for each channel as well as total figures.

## Data Sources (Inputs)
- ← [[AGR.AG_EDR]]
| Column Name |
|---|
| PERIOD_ID |
| SUBSCR_ID |
| TIERID_3 |
| NUMBER_OF_EDR |
| TOTAL_AMOUNT |
| CATEGORY |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |

