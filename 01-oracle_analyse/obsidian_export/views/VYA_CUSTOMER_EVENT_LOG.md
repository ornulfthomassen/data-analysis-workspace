# VYA_CUSTOMER_EVENT_LOG

**Schema:** `CCM` | **Type:** `View`

## Description
This view, VYA_CUSTOMER_EVENT_LOG, consolidates detailed customer event data by joining event details with event type, event medium, and customer mapping information. It transforms and formats event dates, derives a customer surrogate key (CUSTOMER_SK), and provides hierarchical event descriptions. The view specifically filters for customer events that occurred within the last 30 days, making it suitable for analyzing recent customer interactions or for loading into other systems for near-real-time processing.

## Data Sources (Inputs)
- ← [[CCDW_CUSTOMER_EVENT.CUSTOMER_EVENT_DETAIL]]
- ← [[CCDW_CUSTOMER_EVENT.EVENT_TYPE]]
- ← [[CCDW_CUSTOMER_EVENT.EVENT_MEDIUM]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]

