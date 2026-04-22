# GCP_TALKMORE_SUBSCR_MOBILE

**Schema:** `CCM` | **Type:** `View`

## Description
This view serves to provide a standardized and cleaned representation of mobile subscription data. It selects all columns from the `INVENTORY_SUBSCR_MOBILE` table, applies a `TRIM()` function to various ID-related fields to remove leading/trailing whitespace, and renames the columns with a consistent `TALKMORE_` prefix for better clarity and integration, likely for downstream reporting or system consumption (e.g., in a GCP context as suggested by the view name).

## Data Sources (Inputs)
- ← [[TALKMORE.INVENTORY_SUBSCR_MOBILE]]

