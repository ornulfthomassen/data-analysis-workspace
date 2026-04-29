# GTIN_DEVICE

**Schema:** `CCM` | **Type:** `View`

## Description
Combines device GTIN (Global Trade Item Number) information with its detailed properties, specifically extracting a truncated IMEI, the GTIN itself, and various GTIN-related attributes like manufacturer, model, color, and size, for devices with a 15-character IMEI.

## Data Sources (Inputs)
- ← [[fps.terminal_gtin]]
| Column Name |
|---|
| imei |
| gtin |
- ← [[fps.terminal_gtin_properties]]
| Column Name |
|---|
| manufacturer |
| model_name |
| color_name |
| total_size |
| gtin |

