# BALANCEW01_TALKMORE_W_AGG

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure aggregates 'Talkmore' subscription balance data on a weekly basis and stores it in the 'BALANCE_TALKMORE_WEEK_AGG' table within the 'CLM_ADM' schema. It manages the table's partitions dynamically, creating the table if it doesn't exist, dropping and recreating partitions for specific weeks, and then inserting aggregated data into these partitions. The aggregation involves counting distinct directory numbers based on subscription validity and product details for 'Talkmore' products.

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
- → [[CLM_ADM.BALANCE_TALKMORE_WEEK_AGG]]
| Column Name |
|---|
| REFRESH_DATE |
| PERIOD_WEEK_KEY |
| YEAR_WEEK |
| YEAR_MONTH |
| PRIM_PRODUCT_DESC |
| DRM_COMMON_PAYMENT |
| DRM_COMMON_BRAND |
| BALANCE |

