# GCP_TALKMORE_SUBSCR_BROADBAND

**Schema:** `CCM` | **Type:** `View`

## Description
This view retrieves and standardizes broadband subscription inventory data. It selects all relevant columns from the source table, trims leading/trailing spaces from several string fields, and renames columns with more descriptive names (e.g., prefixed with 'TALKMORE_'). Essentially, it provides a cleansed and aliased projection of the raw broadband subscription inventory.

## Data Sources (Inputs)
- ← [[TALKMORE.INVENTORY_SUBSCR_BROADBAND]]

