# PI_NW_YNG_UP

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates the count of specific 'new young subscription' sales ('antall') by joining subscription offer incentive data with product offer details. It filters for recent incentives, a specific parameter ID, a particular product offer category, and a predefined list of product offer IDs. The results are grouped by product offer ID and public name.

## Data Sources (Inputs)
- ← [[cm.subscription_offer_incentive]]
| Column Name |
|---|
| PRODUCT_OFFER_ID |
| inc_valid_from_date |
| parameter_id |
- ← [[pcat.product_offer]]
| Column Name |
|---|
| product_offer_id |
| public_name |
| product_offer_category_id |

