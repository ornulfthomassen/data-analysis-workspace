# VYA_ORDER_LINE_DETAIL_FACT_NB

**Schema:** `CCM` | **Type:** `View`

## Description
This view is designed to identify and construct detailed order line fact records for 'Nettbutikken' (webshop) device sales that are *not* already present in the main `ORDER_LINE_DETAIL_FACT_MV` table. It synthesizes these records by taking device delivery information from `VYA_INSIGHT_DEVICE_FROM_NB`, populating many order-related fields with default, hardcoded, or derived values, and marking them as 'new sales' of devices. Its primary purpose is to ensure all webshop device sales, especially those without traditional order entries, are included in the overall order line detail data.

## Data Sources (Inputs)
- ← [[CCM.VYA_INSIGHT_DEVICE_FROM_NB]]
- ← [[GALAXY.DEVICE_DIM]]
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.DEALER_DIM]]

