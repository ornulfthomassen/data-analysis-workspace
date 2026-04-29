# P_CU_CCM_CUST_CHL_INTERACTION

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Aggregates customer channel interaction data from a staging table, performs data retention housekeeping on the staging table, and updates a permanent aggregated table using a table swap strategy, which includes index and grant management, based on row count deviation thresholds.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_CUST_CHANNEL_INTERACTION]]
- ← [[CLM_CCM.STG_CUST_CHL_INTERACTION]]
| Column Name |
|---|
| KURT_ID_EVENT |
| PERIOD_KEY |
| EVENT_DATE |
| EVENT_MEDIUM_DESC |

## Target Tables (Outputs)
- → [[CLM_CCM.STG_CUST_CHL_INTERACTION]]
| Column Name |
|---|
| PERIOD_KEY |
- → [[CLM_CCM.CCM_CUST_CHANNEL_INTERACTION_N]]
| Column Name |
|---|
| KURT_ID |
| APP_LAST_USED_DATE |
| APP_PERIOD_KEY_CURRENT_MO |
| NO_DAYS_USED_APP_CURRENT_MO |
| NO_DAYS_USED_APP_PREV_MO_1 |
| NO_DAYS_USED_APP_PREV_MO_2 |
| NO_DAYS_USED_APP_PREV_MO_3 |
| APP_MEDIUM_LAST_USED |
| LOAD_DTTM |
- → [[CLM_CCM.CCM_CUST_CHANNEL_INTERACTION_O]]
- → [[CLM_CCM.CCM_CUST_CHANNEL_INTERACTION]]
| Column Name |
|---|
| KURT_ID |
| APP_LAST_USED_DATE |
| APP_PERIOD_KEY_CURRENT_MO |
| NO_DAYS_USED_APP_CURRENT_MO |
| NO_DAYS_USED_APP_PREV_MO_1 |
| NO_DAYS_USED_APP_PREV_MO_2 |
| NO_DAYS_USED_APP_PREV_MO_3 |
| APP_MEDIUM_LAST_USED |
| LOAD_DTTM |

