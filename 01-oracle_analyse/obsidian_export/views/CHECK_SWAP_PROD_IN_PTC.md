# CHECK_SWAP_PROD_IN_PTC

**Schema:** `CCM` | **Type:** `View`

## Description
Identifies and counts 'SWAP' device product offers from subscribed products that are present in `galaxy.product_dim` but are NOT found in the `ptc` table. It essentially checks for subscribed 'SWAP' devices that are missing from the `ptc` reference.

## Data Sources (Inputs)
- ← [[ccdw.subscribed_product]]
- ← [[galaxy.product_dim]]
- ← [[ptc]]

