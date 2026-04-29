# VYA_PREPAID_CHARGING_METHODS

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates prepaid charging method data by period and traffic type, filtering for specific traffic categories ('EDR', 'Ladinger'). It calculates the sum of gross amounts, and counts of accounts and charging events for each aggregated group.

## Data Sources (Inputs)
- ← [[CCDW_USAGE.MOBILE_SUBSCR_CHARGE_MONTH]]
| Column Name |
|---|
| PERIOD_ID |
| TRAFFIC_TYPE_ID |
| GROSS_AMOUNT |
| ACCOUNT_ID |
| NUMBER_OF_EVENTS |
- ← [[GALAXY.TRAFFIC_TYPE_DIM_V]]
| Column Name |
|---|
| TRAFFIC_TYPE_NAME_3 |
| TRAFFIC_TYPE_KEY |
| TRAFFIC_TYPE_NAME_1 |
| TRAFFIC_TYPE_NAME_2 |

