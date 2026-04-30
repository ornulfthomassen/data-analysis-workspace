# KIM_DATAKONTROLL_HISTORY_V

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a view that combines subscription details with product offer names for a specific product offer (ID 7096079), providing subscription keys, product keys, product offer names, and start/end dates.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PRODUCT_OFFER_ID |
| START_DATE |
| END_DATE |

- ← [[CCDW.PRODUCT_OFFER]]
| Column Name |
|---|
| PRODUCT_OFFER_ID |
| PRODUCT_OFFER_NAME |


