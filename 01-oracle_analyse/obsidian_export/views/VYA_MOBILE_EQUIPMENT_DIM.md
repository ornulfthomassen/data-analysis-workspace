# VYA_MOBILE_EQUIPMENT_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `VYA_MOBILE_EQUIPMENT_DIM`, serves as a comprehensive dimension table for mobile equipment. Its primary purpose is to consolidate and enrich device (handset) information from various sources for data warehousing or analytical loading ('LOADING Device DIM-DATA TO MJØSA'). It combines core device attributes, cleanses textual fields (e.g., marketing names, manufacturers), standardizes device types (e.g., 'PDA' to 'Smartphone'), and calculates launch dates based on the earliest known sales start or historical data. It also ensures that all handset keys found in order line details are included, even if they don't yet exist in the main device dimension, marking them as 'Ukjent' (Unknown).

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_DEVICE_DIM]]
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
- ← [[CLM_ADM.ADM_DEVICE_RANGE_DIM]]
- ← [[GALAXY.HANDSET_DIM_V]]
- ← [[CLM_ADM.ADM_HANDSET_HIST_AGG]]

