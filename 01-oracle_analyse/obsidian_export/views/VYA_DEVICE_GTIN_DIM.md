# VYA_DEVICE_GTIN_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
Loads and cleanses Global Trade Item Number (GTIN) related device information, including unique International Mobile Equipment Identity (IMEI) values, memory size, and color name, from the FPS system's terminal data tables for use in Viya.

## Data Sources (Inputs)
- ← [[FPS.TERMINAL_GTIN]]
| Column Name |
|---|
| IMEI |
| GTIN |
- ← [[FPS.TERMINAL_GTIN_PROPERTIES]]
| Column Name |
|---|
| GTIN |
| TOTAL_SIZE |
| COLOR_NAME |

