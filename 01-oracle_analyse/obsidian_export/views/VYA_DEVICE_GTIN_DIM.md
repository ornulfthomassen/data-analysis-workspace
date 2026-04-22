# VYA_DEVICE_GTIN_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
Loads GTIN (Global Trade Item Number) information, including color and memory size, for unique devices from the FPS system into Viya. It derives full IMEI and IMEI_USE, applying cleansing and validation rules for IMEI values.

## Data Sources (Inputs)
- ← [[FPS.TERMINAL_GTIN]]
- ← [[FPS.TERMINAL_GTIN_PROPERTIES]]

