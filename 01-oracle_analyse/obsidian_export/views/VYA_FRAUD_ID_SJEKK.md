# VYA_FRAUD_ID_SJEKK

**Schema:** `CCM` | **Type:** `View`

## Description
Retrieves and presents detailed order and customer identification information, enriched with descriptive labels for identification types and customer types, primarily to support fraud investigation by allowing fraud managers to check ID information associated with orders. It also attempts to categorize the nature of the ID number (e.g., if it's a birthdate).

## Data Sources (Inputs)
- ← [[ONL_REP.SERVICE_ORDER]]
- ← [[CCDW_ORDER.ORDER_STATUS]]
- ← [[CCDW_ORDER.ORDER_STATUS_REASON]]
- ← [[CCDW_ORDER.ORDER_ACTION_TYPE]]

