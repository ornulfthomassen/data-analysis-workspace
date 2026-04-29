# PP_GCP_MOBILE_ORDER_LINE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Prepares and loads monthly mobile order line data into a partitioned fact table (`CLM_ADM.GCP_MOBILE_ORDER_LINE`). It first materializes product and mobile equipment dimensions into temporary tables (`CLM_ADM.TMP_PRODUCT_DIM`, `CLM_ADM.TMP_MOB_EQUIPMENT_DIM`), then iterates through a specified month range. For each month and for five distinct sub-partition types ('AO', 'SO', 'FT', 'HW', 'NB'), it dynamically creates partitions/subpartitions in the target table if they don't exist. It then invokes an external procedure (`CLM_ADM.PP_GCP_TMP_MOBILE_ORDER_LINE`) to populate another temporary table (`CLM_ADM.TMP_MOBILE_ORDER_LINE`) using the materialized dimension data. Finally, it uses `ALTER TABLE ... EXCHANGE SUBPARTITION` to efficiently move the data from `CLM_ADM.TMP_MOBILE_ORDER_LINE` into the corresponding subpartitions of `CLM_ADM.GCP_MOBILE_ORDER_LINE`.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| YEAR_MONTH_NUMBER |
- ← [[CCM.VYA_PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_SK |
| PRODUCT_BRAND |
| PRODUCT_PAYMENT |
| PRODUCT_AREA |
| PRODUCT_CATEGORY |
| PRODUCT_GROUP |
| PRODUCT_MARKET_NAME |
| PRODUCT_REPORTING |
| PRODUCT_MONTHLY_FEE |
| PRODUCT_PRIMARY_FLAG |
| PRODUCT_DESC |
| PRODUCT_FAMILY_NAME |
| PRODUCT_NAME |
| PRODUCT_PAYTYPE |
| PRODUCT_POID |
| PRODUCT_TK_INCOME_SERVICE |
| PRODUCT_TK_PRODUCT_RANK |
| PRODUCT_STARTUP_FEE |
- ← [[CCM.VYA_MOBILE_EQUIPMENT_DIM]]
| Column Name |
|---|
| HANDSET_SK |
| DEVICE_MANUFACTURER |
| DEVICE_MARKETING_NAME |
| DEVICE_CATEGORY |
| DEVICE_CAMERA_INFO |
| DEVICE_RANGE |
| DEVICE_TYPE |

## Target Tables (Outputs)
- → [[CLM_ADM.TMP_PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_SK |
| PRODUCT_BRAND |
| PRODUCT_PAYMENT |
| PRODUCT_AREA |
| PRODUCT_CATEGORY |
| PRODUCT_GROUP |
| PRODUCT_MARKET_NAME |
| PRODUCT_REPORTING |
| PRODUCT_MONTHLY_FEE |
| PRODUCT_PRIMARY_FLAG |
| PRODUCT_DESC |
| PRODUCT_FAMILY_NAME |
| PRODUCT_NAME |
| PRODUCT_PAYTYPE |
| PRODUCT_POID |
| PRODUCT_TK_INCOME_SERVICE |
| PRODUCT_TK_PRODUCT_RANK |
| PRODUCT_STARTUP_FEE |
- → [[CLM_ADM.TMP_MOB_EQUIPMENT_DIM]]
| Column Name |
|---|
| HANDSET_SK |
| DEVICE_MANUFACTURER |
| DEVICE_MARKETING_NAME |
| DEVICE_CATEGORY |
| DEVICE_CAMERA_INFO |
| DEVICE_RANGE |
| DEVICE_TYPE |
- → [[CLM_ADM.GCP_MOBILE_ORDER_LINE]]

