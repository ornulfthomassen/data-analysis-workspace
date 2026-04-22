# VYA_USAGE_DAY

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view, `VYA_USAGE_DAY`, serves as a direct alias or a wrapper view for `clm_ccm.VA_USAGE_DAY`. It selects all columns from the source view, effectively re-exposing daily usage data, including volume metrics (e.g., total volume, volume down, volume in MB), daily and weekly temporal information, subscription identifiers, product details (name, offer, payment, reporting, category, group, family, price, POID, reporting codes), included data, and device characteristics (camera, type, manufacturer, OS, class). Its primary purpose is likely to provide access to this detailed daily usage information under a different schema (`CLM_ADM`) or for abstraction/security purposes.

## Data Sources (Inputs)
- ← [[clm_ccm.VA_USAGE_DAY]]

