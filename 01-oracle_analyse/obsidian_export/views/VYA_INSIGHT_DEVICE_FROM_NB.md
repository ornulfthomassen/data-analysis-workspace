# VYA_INSIGHT_DEVICE_FROM_NB

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a curated list of sold handset details. It filters records to include only those originating from the 'NB' file source. For each unique IMEI, it selects only the most recent (latest delivered) record, effectively de-duplicating entries and presenting the latest known status or sale for a device. The view also performs extensive data type casting, formatting, and extraction of date components (year, year-month) and IMEI parts (full, use, handset key) into specific formats and lengths.

## Data Sources (Inputs)
- ← [[THIRD_PARTY_SERVICES.SOLD_HANDSETS]]

