# VYA_INSIGHT_DEVICE_FROM_NB_TB

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a curated and deduplicated list of sold handset records, specifically for devices originating from the 'NB' file source. For each unique IMEI, it selects the most recent record based on the handset delivered date, effectively filtering out older or potentially superseded entries. The view includes detailed information about the handset, invoice, and dealer, along with various derived date components and different representations of the IMEI.

## Data Sources (Inputs)
- ← [[THIRD_PARTY_SERVICES.SOLD_HANDSETS]]

