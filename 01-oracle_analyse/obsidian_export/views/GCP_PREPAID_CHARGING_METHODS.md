# GCP_PREPAID_CHARGING_METHODS

**Schema:** `CCM` | **Type:** `View`

## Description
Provides aggregated report data on prepaid charging methods/recharges for specific traffic types, intended for SAS Viya reporting. It summarizes included VAT amount, counts of accounts, and counts of recharges by period and traffic type.

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
| TRAFFIC_TYPE_KEY |
| TRAFFIC_TYPE_NAME_3 |
| TRAFFIC_TYPE_NAME_1 |
| TRAFFIC_TYPE_NAME_2 |

