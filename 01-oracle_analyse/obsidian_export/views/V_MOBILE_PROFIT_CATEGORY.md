# V_MOBILE_PROFIT_CATEGORY

**Schema:** `CCM` | **Type:** `View`

## Description
This view combines subscription mapping data with categorized profit data. It links profit categories to specific subscriptions, calculates a monthly period key and a 'profit period' key (two months prior) based on a period ID, and filters for a specific source system.

## Data Sources (Inputs)
- ← [[PROFIT.CP_CAT_BED_PRIV]]
| Column Name |
|---|
| SUBSCR_ID |
| PERIOD_ID |
| CATEGORY |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |
| SUBSCRIPTION_ID |

