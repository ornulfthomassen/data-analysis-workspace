# TEST_CCM_SUBS_DATA

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates subscriber usage and revenue metrics for the current month, previous month, and two months prior, providing a historical snapshot. It calculates sums for small screen volume, SMS count, data download volume, total data volume, total voice minutes, compensated voice minutes, and gross revenue, grouped by main number, user customer key, and the owner's ID. The data is filtered for a specific month (201305) and for valid main numbers and user customer keys, joined with subscription information.

## Data Sources (Inputs)
- ← [[CCDW_CONSUMERANALYSE.CON_USAGE_AGG]]
| Column Name |
|---|
| main_number |
| user_customer_key |
| MOB_SMALL_SCR_VOL |
| MOB_SMS_NUM |
| VOLUME_DOWN |
| VOLUME_TOTAL |
| MOB_TOT_MIN |
| MOB_COMP_CALLS_MIN |
| GROSS_REVENUE |
| SUBSCRIPTION_KEY |
| PERIOD_MONTH_KEY |
- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| KURT_ID_OWNER |
| SUBSCRIPTION_ID |
| START_DATE |
| END_DATE |

