# GCP_MOBILE_EQUIPMENT_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `GCP_MOBILE_EQUIPMENT_DIM`, serves as a consolidated and enriched dimension table for mobile equipment (handsets/devices). It combines detailed device attributes from a primary administrative device dimension with information about 'unknown' devices identified from order data. The view cleanses string data (e.g., replaces special characters in names), standardizes device types (e.g., 'PDA' to 'Smartphone'), and calculates launch dates based on various sources. Its primary purpose is to prepare and provide comprehensive device dimension data for loading into an analytical platform or data warehouse (referred to as Mjøsa/GCP).

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_DEVICE_DIM]]
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
- ← [[CLM_ADM.ADM_DEVICE_RANGE_DIM]]
- ← [[GALAXY.HANDSET_DIM_V]]
- ← [[CLM_ADM.ADM_HANDSET_HIST_AGG]]

