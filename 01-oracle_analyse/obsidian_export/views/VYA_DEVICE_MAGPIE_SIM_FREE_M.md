# VYA_DEVICE_MAGPIE_SIM_FREE_M

**Schema:** `CCM` | **Type:** `View`

## Description
This view processes and standardizes 'SIM-free' mobile device deal data by aggregating pricing information, cleansing device attributes (manufacturer, model, capacity), and attempting to match these devices to Global Trade Item Number (GTIN) properties. It uses multiple fuzzy matching strategies to link device deals to GTINs and combines this with date dimension data, ultimately preparing a consolidated dataset of standardized device deals for analysis or loading into a data warehouse (referred to as MJØSA in the script's comments).

## Data Sources (Inputs)
- ← [[THIRD_PARTY_SERVICES.MAGPIE_DEVICE_PRICE]]
- ← [[FPS.TERMINAL_GTIN_PROPERTIES]]
- ← [[GALAXY.DATE_DIM_MV]]

