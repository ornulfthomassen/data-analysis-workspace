# P_GOV_DQ_MARTS_INS_CHURN_CHECK

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This procedure performs data quality checks on churn reporting data for weekly periods. It verifies the existence of required data partitions for the current and previous weeks. If partitions are missing, it logs an 'ERROR' status. If partitions exist, it calculates and compares various churn and balance metrics (e.g., total balance, churn counts, churn percentages for different brands and profit categories) between the current and previous week. Based on predefined thresholds for these differences, it determines a data quality 'status' ('OK' or 'Not OK') and a detailed 'reason' message, then logs this information into a data quality mart table.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OWNER |
| OBJECT_NAME |
| SUBOBJECT_NAME |

- ← [[CCM.DUAL]]
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_WEEK_NUMBER |

- ← [[CRM_ANALYSE.BALANCE_MOBILE_SEGMENT_W_AGG]]
| Column Name |
|---|
| period_week_key |
| balance |
| out_port |
| drm_common_brand |
| profit_cat_name2 |


## Target Tables (Outputs)
- → [[CLM_CCM.GOV_DQ_MARTS]]
| Column Name |
|---|
| RUNTIME |
| FREQ |
| SYSTEM_NM |
| PROCESS_NM |
| STATUS_NM |
| REASON |
| PRIORITY |
| START_TIME |
| END_TIME |
| PREV_OK_DTTM |
| PREV_OK_RESSULT |
| LAST_RESSULT |


