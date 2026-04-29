# VYA_HW_PR_TR_GTIN_OVRD_EXT_RET_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view extracts and transforms data from the HW_PRICE_TIER_GTIN_OVERRIDE_EXT_RETAIL table, casting various columns to specific VARCHAR or NUMBER types and formats. It appears to standardize or prepare 'GTIN Override' related product and pricing information, including GTIN, RRP (Recommended Retail Price) values, tier, validity periods, source, manufacturer, model, color, size, and insertion details, likely for external use or reporting.

## Data Sources (Inputs)
- ← [[CLM_SID.HW_PRICE_TIER_GTIN_OVERRIDE_EXT_RETAIL]]
| Column Name |
|---|
| GTIN |
| RRP_EX_VAT |
| RRP_INC_VAT |
| TIER |
| VALID_FROM |
| VALID_TO |
| SOURCE |
| MANUFACTURER |
| MODEL_NAME |
| COLOR_NAME |
| TOTAL_SIZE |
| INSERTED_BY |
| INSERTED_DTTM |

