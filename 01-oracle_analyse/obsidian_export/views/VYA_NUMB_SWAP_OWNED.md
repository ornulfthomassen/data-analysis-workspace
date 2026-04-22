# VYA_NUMB_SWAP_OWNED

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates the number of active 'SWAP' devices owned by each customer, along with the earliest and latest end dates for these swaps. It identifies 'SWAP' devices based on product group ('DEVICE') and market product ('SWAP') status, and filters for active products.

## Data Sources (Inputs)
- ← [[CLM_CCM.V_ODS_AGRMT_OFFER_MOB_DEVICE]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]

