# GCP_MOBILE_EQUIPMENT_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates and enriches mobile equipment (handset) dimension data. It combines core device attributes from an administrative device dimension table with handset keys from order details, categorizing unknown handsets as 'Ukjent'. It also integrates device range information, calculates launch dates based on marketing names or historical aggregates, and provides derived date components, ultimately preparing a comprehensive dataset for a mobile equipment dimension in a data warehouse or analytical system.

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

