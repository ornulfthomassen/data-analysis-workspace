# VYA_INSIGHT_DEVICE_FROM_USE

**Schema:** `CCM` | **Type:** `View`

## Description
This view extracts unique device (IMEI) usage information, linking it to subscription details, market area, and product data. It consolidates IMEI-related attributes (like handset key, full IMEI, first/last use dates) and enriches them with subscription identifiers and market/product classifications by joining with subscription mapping and ODS subscription data. The primary goal is to provide a unified dataset of devices based on their usage.

## Data Sources (Inputs)
- ← [[LIVE.EUREKA_IMEI]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[ODS.SUBSCRIPTION_ODS_MOB]]

