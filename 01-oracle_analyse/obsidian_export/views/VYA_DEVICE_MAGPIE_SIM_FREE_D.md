# VYA_DEVICE_MAGPIE_SIM_FREE_D

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a filtered, standardized, and enriched dataset of 'SIM-free' device pricing information. It aggregates raw device pricing data, cleans and normalizes device names and specifications, filters for new devices with certain upfront cost criteria, and matches these devices against Global Trade Item Number (GTIN) properties. The output includes various pricing metrics (min, max, average, median upfront costs), device characteristics, vendor details, and GTIN identifiers, along with a 'hit level' indicating the confidence of the GTIN match. The view is designed to be loaded into a data warehouse for further analysis of device prices.

## Data Sources (Inputs)
- ← [[THIRD_PARTY_SERVICES.MAGPIE_DEVICE_PRICE]]
| Column Name |
|---|
| BRAND_NAME |
| DEVICE_NAME_STANDARDISED |
| DEVICE_CAPACITY |
| DATE_FOUND |
| VENDOR |
| DESTINATION_VENDOR |
| NETWORK |
| TARIFF_NAME |
| TOTAL_UPFRONT_COST |
| DEAL_URL |
| ONLINE_ONLY_DEAL |
| EXISTING_CUSTOMERS_ONLY |
| AVAILABILITY |
| FREE_GIFT |
| OTHER_INFO |
| EFFECTIVE_MONTHLY_COST |
| DEVICE_NAME_AS_SOLD |
| DEVICE_COLOUR |
| DEVICE_CONDITION |
- ← [[FPS.TERMINAL_GTIN_PROPERTIES]]
| Column Name |
|---|
| MANUFACTURER |
| MODEL_NAME |
| TOTAL_SIZE |
| GTIN |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |

