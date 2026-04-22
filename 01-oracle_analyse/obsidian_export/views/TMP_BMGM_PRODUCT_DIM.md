# TMP_BMGM_PRODUCT_DIM

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view serves as a unified product dimension table, consolidating and classifying products from various source systems ('Pacman', 'deFakto', 'KAS') based on their attributes. It derives new columns such as 'ROLLE' (USER/OWNER) and several numeric flags (e.g., NUM_PRIV_POSTPAID_SUBS_OWNED, NUM_SWAP_AGREEMENTS_OWNED, NUM_FIXED_BROADBAND_OWNED) which indicate specific product types or usage characteristics (e.g., private postpaid subscription, swap agreement, mobile broadband, fixed broadband, fixed telephony) based on a complex set of business rules involving product area, category, payment type, and reporting classifications.

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]

