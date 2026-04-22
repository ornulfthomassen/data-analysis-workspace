# P_DISCOUNT_PRODUCT_DIM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `P_DISCOUNT_PRODUCT_DIM` is designed to create or refresh a dimension table named `DISCOUNT_PRODUCT_DIM`. It first checks for the existence of the table and drops it if found, then recreates it using a `CREATE TABLE AS SELECT` statement. This statement populates the dimension table with aggregated product discount information, including price overrides, deductions, and percentage deductions, derived from product offer configurations. Finally, it gathers statistics on the newly created table and attempts to create indexes.

## Data Sources (Inputs)
- ← [[PCAT.PRODUCT_OFFER]]
- ← [[PCAT.V_PRODUCT_OFFER_CONFIG_MV]]
- ← [[GALAXY.PRODUCT_DIM]]

## Target Tables (Outputs)
- → [[DISCOUNT_PRODUCT_DIM]]

