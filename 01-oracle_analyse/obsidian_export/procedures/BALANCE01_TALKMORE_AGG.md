# BALANCE01_TALKMORE_AGG

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure creates a partitioned aggregate table `BALANCE_TALKMORE_AGG` if it does not exist. It then iterates through a range of months (either specified by parameters or defaulting to the previous month), dropping and re-adding partitions for each month in the target table. Finally, it inserts aggregated 'Talkmore' subscription balance data from the `CM.SUBSCRIPTION` and `CM.PROD_SERV_MAPPING` tables into the newly prepared partition for the respective month.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
| SUBOBJECT_NAME |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| DATE_KEY |
| YEAR_MONTH_NUMBER |
- ← [[CM.SUBSCRIPTION]]
| Column Name |
|---|
| S212_PRODUCT_ID |
| SUBSCR_VALID_FROM_DATE |
| SUBSCR_VALID_TO_DATE |
| DIRECTORY_NUMBER_ID |
- ← [[CM.PROD_SERV_MAPPING]]
| Column Name |
|---|
| PRODUCT_UNIT_ID |
| PRODUCT_DESCR |
| PRODUCT_PREPAID |

## Target Tables (Outputs)
- → [[CLM_ADM.BALANCE_TALKMORE_AGG]]
| Column Name |
|---|
| REFRESH_DATE |
| PERIOD_MONTH_KEY |
| YEAR_MONTH |
| PRIM_PRODUCT_DESC |
| DRM_COMMON_PAYMENT |
| DRM_COMMON_BRAND |
| BALANCE |

