# VYA_DEVICE_MAGPIE_SIM_FREE_D

**Schema:** `CCM` | **Type:** `View`

## Description
Extracts, standardizes, and enriches 'SIM-free' mobile phone device pricing and availability data from a third-party source. It filters for new, non-tablet/non-watch devices with an upfront cost, and attempts to match these devices to internal GTIN (Global Trade Item Number) properties for identification, providing various upfront cost metrics (min, max, avg, median) and deal-specific information.

## Data Sources (Inputs)
- ← [[THIRD_PARTY_SERVICES.MAGPIE_DEVICE_PRICE]]
- ← [[FPS.TERMINAL_GTIN_PROPERTIES]]
- ← [[GALAXY.DATE_DIM_MV]]

