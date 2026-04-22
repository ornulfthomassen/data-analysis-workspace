# VYA_HW_PR_TR_GTIN_OVRD_EXT_RET_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view standardizes and formats data related to hardware price tier GTIN overrides for external retail. It converts various fields like GTIN, RRP (Recommended Retail Price) excluding and including VAT, price tier, valid dates, manufacturer, model, and insertion details into specific data types and formats (primarily VARCHAR and NUMBER), often handling potential data inconsistencies like comma-separated decimals for RRP. The output provides a clear, consistent set of 'override' information.

## Data Sources (Inputs)
- ← [[CLM_SID.HW_PRICE_TIER_GTIN_OVERRIDE_EXT_RETAIL]]

