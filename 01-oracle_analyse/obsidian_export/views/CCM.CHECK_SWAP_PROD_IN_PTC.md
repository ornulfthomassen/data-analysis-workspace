# CHECK_SWAP_PROD_IN_PTC

**Schema:** `CCM` | **Type:** `View`

## Description
Counts the occurrences of product offer IDs from 'ccdw.subscribed_product' that correspond to 'SWAP DEVICE' products found in 'galaxy.product_dim' but are not registered in the 'ptc' table.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
| Column Name |
|---|
| product_offer_id |

- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| product_key |
| drm_common_product_group |
| drm_common_market_product |

- ← [[CCM.PTC]]
| Column Name |
|---|
| id |


