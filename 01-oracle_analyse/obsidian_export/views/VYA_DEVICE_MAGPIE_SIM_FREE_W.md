# VYA_DEVICE_MAGPIE_SIM_FREE_W

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates and cleans SIM-free mobile device pricing data from a third-party source, standardizes device information, filters out non-handset devices (e.g., watches, tablets, enterprise models), and enriches records with Global Trade Item Numbers (GTINs) and date dimensions. The resulting dataset is intended for analytical purposes, specifically for loading into a data warehouse named 'MJØSA'. It calculates various upfront cost metrics (max, min, avg, median) and provides details about device availability and deals.

## Data Sources (Inputs)
- ← [[THIRD_PARTY_SERVICES.MAGPIE_DEVICE_PRICE]]
| Column Name |
|---|
| BRAND_NAME |
| DEVICE_NAME_STANDARDISED |
| DEVICE_CAPACITY |
| DATE_FOUND |
| TOTAL_UPFRONT_COST |
| DEAL_URL |
| ONLINE_ONLY_DEAL |
| EXISTING_CUSTOMERS_ONLY |
| AVAILABILITY |
| FREE_GIFT |
| OTHER_INFO |
| VENDOR |
| DESTINATION_VENDOR |
| NETWORK |
| TARIFF_NAME |
| DEVICE_COLOUR |
| EFFECTIVE_MONTHLY_COST |
| DEVICE_NAME_AS_SOLD |
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
| YEAR_WEEK_NUMBER |
| WEEK_ENDING |

