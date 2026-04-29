# VYA_DEVICE_MAGPIE_SIM_FREE_M

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates and standardizes SIM-free device pricing data from a third-party source, enriches it with GTIN properties through multiple fuzzy matching strategies, and provides detailed device and pricing metrics along with date dimensions for analytical purposes.

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
| YEAR_MONTH_NUMBER |

