# DEVICE_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view (`DEVICE_DIM_V`) serves as a comprehensive device dimension for CRM analysis. It consolidates device attributes from the main `ADM_DEVICE_DIM` table. Crucially, it enriches this dimension by including `HANDSET_KEY`s found in sales order details (`ORDER_LINE_DETAIL_FACT_MV`) that are not present in `ADM_DEVICE_DIM`, labeling their attributes as 'Ukjent' (Unknown). It further enhances the device information with details like device range, calculated launch dates (based on marketing name or historical data), and cleanses certain character encodings in device names. It also normalizes `DEVICE_TYPE`, for example, changing 'PDA' to 'Smartphone'.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_DEVICE_DIM]]
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
- ← [[CLM_ADM.ADM_DEVICE_RANGE_DIM]]
- ← [[GALAXY.HANDSET_DIM_V]]
- ← [[CLM_ADM.ADM_HANDSET_HIST_AGG]]

