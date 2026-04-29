# STOCK_MOBILE_HIST_WEEK2

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure manages and populates weekly historical mobile stock detail data into a partitioned table, `STOCK_MOBILE_HIST_WEEK_DET`. It dynamically creates or recreates weekly partitions for a specified or calculated range of weeks. For each week, it invokes an external procedure (`CLM_ADM.STOCK_MOBILE_HIST2`) to populate a staging table (`STOCK_MOBILE_HIST_DET`) with the relevant weekly data, and then efficiently loads this data into the corresponding partition of `STOCK_MOBILE_HIST_WEEK_DET` using an `ALTER TABLE ... EXCHANGE PARTITION` operation. It also creates a `STOCK_MOBILE_HIST_WEEK_AGG` table if it does not exist, though the logic to populate it is commented out.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
| SUBOBJECT_NAME |
- ← [[DUAL]]
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| DATE_KEY |
| YEAR_WEEK_NUMBER |
- ← [[CLM_ADM.STOCK_MOBILE_HIST_DET]]
| Column Name |
|---|
| REFRESH_DATE |
| DAY |
| PERIOD_DATE_KEY |
| PERIOD_WEEK_KEY |
| PERIOD_MONTH_KEY |
| KURT_ID_OWNER |
| KURT_ID_OWNER_AGE |
| CLM_LIVSFASE_SEGMENT_ID_O |
| MAP2_SEGMENT_ID_O |
| KURT_ID_USER |
| KURT_ID_USER_AGE |
| CLM_LIVSFASE_SEGMENT_ID_U |
| MAP2_SEGMENT_ID_U |
| SUBSCRIPTION_KEY |
| MAIN_NUMBER |
| PRODUCT_KEY |
| PROFIT_CAT_TALE |
| PROFIT_CAT_PAY_TYPE |
| PROFIT_PERIOD |
| VAR_SEGMENT |
| CHURN_SEGMENT |
| KURT_ID_PAYER |
| PAYER_COUNTERPART_KEY |
| FAMILY_BONUS_FLG |

## Target Tables (Outputs)
- → [[CLM_ADM.STOCK_MOBILE_HIST_WEEK_DET]]
| Column Name |
|---|
| REFRESH_DATE |
| DAY |
| PERIOD_DATE_KEY |
| PERIOD_WEEK_KEY |
| PERIOD_MONTH_KEY |
| KURT_ID_OWNER |
| KURT_ID_OWNER_AGE |
| CLM_LIVSFASE_SEGMENT_ID_O |
| MAP2_SEGMENT_ID_O |
| KURT_ID_USER |
| KURT_ID_USER_AGE |
| CLM_LIVSFASE_SEGMENT_ID_U |
| MAP2_SEGMENT_ID_U |
| SUBSCRIPTION_KEY |
| MAIN_NUMBER |
| PRODUCT_KEY |
| PROFIT_CAT_TALE |
| PROFIT_CAT_PAY_TYPE |
| PROFIT_PERIOD |
| VAR_SEGMENT |
| CHURN_SEGMENT |
| KURT_ID_PAYER |
| PAYER_COUNTERPART_KEY |
| FAMILY_BONUS_FLG |

