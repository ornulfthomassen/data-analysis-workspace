# VYA_DEVICE_MAGPIE_SIM_FREE

**Schema:** `CCM` | **Type:** `View`

## Description
Consolidates device and deal information, specifically for 'SIM-free' devices, by combining data from three underlying sources which appear to represent monthly, weekly, and daily granularities of the same data structure. It aggregates all records from these sources into a single view without de-duplication (due to UNION ALL).

## Data Sources (Inputs)
- ← [[CCM.VYA_DEVICE_MAGPIE_SIM_FREE_M]]
- ← [[CCM.VYA_DEVICE_MAGPIE_SIM_FREE_W]]
- ← [[CCM.VYA_DEVICE_MAGPIE_SIM_FREE_D]]

