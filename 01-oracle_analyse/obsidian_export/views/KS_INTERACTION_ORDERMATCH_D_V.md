# KS_INTERACTION_ORDERMATCH_D_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `KS_INTERACTION_ORDERMATCH_D_V`, is designed to identify and display interaction records that have not been successfully matched with specific order criteria or other related data. It selects all columns from the `ks_interaction` table (aliased as 'I') and explicitly sets a large number of order-related and product-related columns to NULL. The core logic is to filter out any interactions that are present in the `KS_INTERACTION_ORDERMATCH_C_V` view based on their `INTERACTION_SEGMENT_ID`. Essentially, it provides a 'default' or 'unmatched' set of interaction details.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ks_interaction]]
- ← [[KS_INTERACTION_ORDERMATCH_C_V]]

