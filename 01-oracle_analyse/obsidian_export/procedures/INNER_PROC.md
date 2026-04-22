# INNER_PROC

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The script defines a procedure `inner_proc`. Its primary intended functionality, as suggested by the fragmented dynamic SQL, is to create a permanent table named `tmppp`. This table would be populated by aggregating configuration values from product offers, specifically `min_configuration_value`, `max_configuration_value`, and `ny_pris` (a sum of distinct configuration values). The source data for this aggregation comes from `PCAT.PRODUCT_OFFER` and `PCAT.V_PRODUCT_OFFER_CONFIG_MV`, filtered for a specific product offer category and ID (2 and 77755 respectively). Additionally, the procedure alters the session's NLS numeric characters. It is important to note that the provided script snippet is incomplete and syntactically malformed, making direct execution impossible as presented.

## Data Sources (Inputs)
- ← [[PCAT.PRODUCT_OFFER]]
- ← [[PCAT.V_PRODUCT_OFFER_CONFIG_MV]]

## Target Tables (Outputs)
- → [[tmppp]]

