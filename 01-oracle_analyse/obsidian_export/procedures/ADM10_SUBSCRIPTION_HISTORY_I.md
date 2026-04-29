# ADM10_SUBSCRIPTION_HISTORY_I

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure processes monthly mobile subscription history data, calculating the latest subscription details for each main number. It then loads this processed data into a dedicated monthly partition of the `ADM_SUBSCRIPTION_HISTORY_I` table, effectively updating or inserting a summary of active subscriptions for the given month.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
| SUBOBJECT_NAME |
- ← [[CRM_ANALYSE.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| FIRST_DATE |
| LAST_DATE |
- ← [[CRM_ANALYSE.TDM_MOBIL_SUBSCR_HIST]]
| Column Name |
|---|
| END_DATE |
| MARKET_AREA_ID |
| MAIN_NUMBER |
| SUBSCRIPTION_ID |
| SUBSCRIPTION_KEY_NEXT |
- ← [[ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| MAIN_NUMBER |
| MARKET_AREA_ID |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.TMP_SUBSCRIPTION_HISTORY_I1]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| END_DATE |
| MARKET_AREA_ID |
| MAIN_NUMBER |
| SUBSCRIPTION_ID |
| SUBSCRIPTION_KEY_NEXT |
- → [[CRM_ANALYSE.TMP_SUBSCRIPTION_HISTORY_I1B]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| END_DATE |
| MARKET_AREA_ID |
| MAIN_NUMBER |
| SUBSCRIPTION_ID |
| SUBSCRIPTION_KEY_NEXT |
- → [[CRM_ANALYSE.TMP_SUBSCRIPTION_HISTORY_I2]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| END_DATE |
| MARKET_AREA_ID |
| MAIN_NUMBER |
| SUBSCRIPTION_ID |
| SUBSCRIPTION_KEY_NEXT |
- → [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY_I]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| END_DATE |
| MARKET_AREA_ID |
| MAIN_NUMBER |
| SUBSCRIPTION_ID |
| SUBSCRIPTION_KEY_NEXT |

