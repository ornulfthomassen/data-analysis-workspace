# MPP_S

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates comprehensive subscription details from the `CCDW.SUBSCRIPTION` table, enriching them with product names and descriptions by joining with the `CLM_CCM.CCM_PRODUCT_TYPE_CONFIG` table twice. It captures various attributes like product offer, market area, owner/payer/user IDs, account information, multiple date fields (start, end, original, change), current status, termination reason, and other operational and agreement-related identifiers, specifically filtering for certain product parent categories.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]

