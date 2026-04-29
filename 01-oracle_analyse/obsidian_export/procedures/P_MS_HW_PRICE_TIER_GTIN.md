# P_MS_HW_PRICE_TIER_GTIN

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This procedure refreshes the 'MS_HW_PRICE_TIER_GTIN' table by performing a "table swap" strategy. It first constructs a new version of the data in a temporary staging table ('MS_HW_PRICE_TIER_GTIN_N') by combining and deduplicating records from multiple source views. It then validates the row count of the new data against the existing table based on a configurable threshold. If the validation passes, the existing 'MS_HW_PRICE_TIER_GTIN' table is renamed to 'MS_HW_PRICE_TIER_GTIN_O' (as a backup), and the staging table 'MS_HW_PRICE_TIER_GTIN_N' is renamed to 'MS_HW_PRICE_TIER_GTIN', making it the new active table. It also manages indexes, grants permissions, gathers statistics, and logs process warnings or errors to a history table.

## Data Sources (Inputs)
- ← [[CLM_CCM.MS_HW_PRICE_TIER_GTIN]]
- ← [[CLM_SID.HW_PRICE_TIER_GTIN_OVERRIDE_V]]
| Column Name |
|---|
| OVERRIDE_GTIN |
| OVERRIDE_MANUFACTURER |
| OVERRIDE_MODEL_NAME |
| OVERRIDE_TOTAL_SIZE |
| OVERRIDE_COLOR_NAME |
| OVERRIDE_RRP_INC_VAT |
| OVERRIDE_INSERTED_DTTM |
| OVERRIDE_TIER |
| OVERRIDE_VALID_FROM |
| OVERRIDE_VALID_TO |
- ← [[CLM_SID.HW_PRICE_TIER_GTIN_V]]
| Column Name |
|---|
| GTIN |
| MANUFACTURER |
| MODEL_NAME |
| TOTAL_SIZE |
| COLOR_NAME |
| TELENOR_RRP_INC_VAT |
| CCDW_LOAD_DATE |
- ← [[CLM_SID.HW_PRICE_TIER_GTIN_OVERRIDE_EXT_RETAIL_V]]
| Column Name |
|---|
| OVERRIDE_GTIN |
| OVERRIDE_MANUFACTURER |
| OVERRIDE_MODEL_NAME |
| OVERRIDE_TOTAL_SIZE |
| OVERRIDE_COLOR_NAME |
| OVERRIDE_RRP_INC_VAT |
| OVERRIDE_INSERTED_DTTM |
| OVERRIDE_TIER |
| OVERRIDE_VALID_FROM |
| OVERRIDE_VALID_TO |
- ← [[ALL_INDEXES]]
| Column Name |
|---|
| OWNER |
| TABLE_NAME |
| INDEX_NAME |

## Target Tables (Outputs)
- → [[CLM_CCM.MS_HW_PRICE_TIER_GTIN_N]]
| Column Name |
|---|
| GTIN |
| Manufacturer |
| Model |
| Sizelol |
| Colour |
| Rrp |
| RrpUpdated |
| Tier |
| OVERRIDE_VALID_FROM |
| OVERRIDE_VALID_TO |
- → [[CLM_CCM.MS_HW_PRICE_TIER_GTIN_O]]
| Column Name |
|---|
| GTIN |
| Manufacturer |
| Model |
| Sizelol |
| Colour |
| Rrp |
| RrpUpdated |
| Tier |
| OVERRIDE_VALID_FROM |
| OVERRIDE_VALID_TO |
- → [[CLM_CCM.MS_HW_PRICE_TIER_GTIN]]
| Column Name |
|---|
| GTIN |
| Manufacturer |
| Model |
| Sizelol |
| Colour |
| Rrp |
| RrpUpdated |
| Tier |
| OVERRIDE_VALID_FROM |
| OVERRIDE_VALID_TO |
- → [[CLM_CCM.CCM_LOAD_HISTORY]]
| Column Name |
|---|
| TABLE_NAME |
| START_DTTM |
| JOB_STATUS |
| STATUS_MESSAGE |
| POWERCENTER_WF_NAME |
| POWERCENTER_S_NAME |

