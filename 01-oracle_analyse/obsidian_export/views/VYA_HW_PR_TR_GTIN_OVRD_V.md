# VYA_HW_PR_TR_GTIN_OVRD_V

**Schema:** `CCM` | **Type:** `View`

## Description
Transforms and standardizes data related to GTIN (Global Trade Item Number) price tier overrides, applying various data type conversions and formatting to present override details like GTIN, RRP (Recommended Retail Price) excluding and including VAT, tier, validity periods, source, manufacturer, model, color, size, and insertion metadata.

## Data Sources (Inputs)
- ← [[CLM_SID.HW_PRICE_TIER_GTIN_OVERRIDE]]
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

