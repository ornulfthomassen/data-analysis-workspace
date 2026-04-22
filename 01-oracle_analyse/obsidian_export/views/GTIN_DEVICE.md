# GTIN_DEVICE

**Schema:** `CCM` | **Type:** `View`

## Description
Retrieves device information by linking IMEI to Global Trade Item Number (GTIN) and its associated product properties (manufacturer, model, color, size). It truncates the IMEI to 14 characters and filters for devices with a 15-character IMEI.

## Data Sources (Inputs)
- ← [[fps.terminal_gtin]]
- ← [[fps.terminal_gtin_properties]]

