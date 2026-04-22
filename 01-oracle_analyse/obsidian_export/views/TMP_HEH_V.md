# TMP_HEH_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Filters and projects specific 'right usage' events from the COMOYO_SUB_GRANT_EVENTS table. It selects event details such as load date, event ID, time, user ID, grantor, SKU information, subscription ID, and right ID. The view specifically includes events where the 'EVENT' type is 'com.comoyo.events.right.RightUsed' and excludes records where the SKU starts with 'CMO-STO-'. It also provides a truncated 100-character string representation of the SKUS column.

## Data Sources (Inputs)
- ← [[COMOYO.COMOYO_SUB_GRANT_EVENTS]]

