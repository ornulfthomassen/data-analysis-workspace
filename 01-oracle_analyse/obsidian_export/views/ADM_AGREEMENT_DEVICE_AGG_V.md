# ADM_AGREEMENT_DEVICE_AGG_V

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates device-related product agreement information from various agreement types (SWAP, Insurance, Downpayment). It counts the total and active agreements for each type, and specifically counts 'Plussforsikring' and 'Skjermforsikring' within the insurance category. It also determines the earliest and latest start dates for active agreements, all grouped by a root agreement identifier.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_STOCK_AGREEMENT_DEVICE_ALL]]
- ← [[GALAXY.PRODUCT_DIM]]

