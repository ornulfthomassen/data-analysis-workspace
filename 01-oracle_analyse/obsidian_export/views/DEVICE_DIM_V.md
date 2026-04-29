# DEVICE_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a comprehensive device dimension view by consolidating device information from administrative device dimensions and order line details. It normalizes device attributes, calculates device launch dates (year, month, and full date) based on marketing name or first period month, and enriches the data with device range and historical aggregation details.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_DEVICE_DIM]]
| Column Name |
|---|
| DEVICE_KEY |
| LOAD_DATE_KEY |
| DEVICE_MANUFACTURER |
| DEVICE_MANUFACTURER_SHORT |
| DEVICE_MARKETING_NAME |
| DEVICE_CATEGORY |
| DEVICE_CLASS |
| DEVICE_OS_INFO |
| DEVICE_TYPE |
| DEVICE_CAMERA_INFO |
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
| Column Name |
|---|
| HANDSET_KEY |
- ← [[CLM_ADM.ADM_DEVICE_RANGE_DIM]]
| Column Name |
|---|
| DEVICE_KEY |
| DEVICE_RANGE |
| MODEL_ID |
| MANUFACTURER |
| MAIN_MODEL_MARKETING_NAME |
- ← [[GALAXY.HANDSET_DIM_V]]
| Column Name |
|---|
| HANDSET_KEY |
| LOCAL_SALES_START_DATE |
- ← [[CLM_ADM.ADM_HANDSET_HIST_AGG]]
| Column Name |
|---|
| MODEL_KEY |
| FIRST_PERIOD_MONTH_KEY |

