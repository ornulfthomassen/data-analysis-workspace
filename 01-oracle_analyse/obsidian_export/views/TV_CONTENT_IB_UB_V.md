# TV_CONTENT_IB_UB_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view calculates and aggregates 'In-Base' (IB) and 'Prior Base' (UB) metrics for TV content volumes. It processes data from the `QLIKVIEW.TV_CONTENT_VOLUME` table, focusing on the first day of each month and the latest available period, then groups and sums these metrics by various product, status, segment, and customer attributes.

## Data Sources (Inputs)
- ← [[QLIKVIEW.TV_CONTENT_VOLUME]]
| Column Name |
|---|
| PERIOD |
| PRODUCT_KEY |
| S |
| STATUS |
| UNIT_PRICE |
| SEGMENT |
| CUSTOMER_SEGMENT |
| CUSTOMER_TYPE |
| GP_STATUS |
| DECODER_STATUS |
| AMOUNT |

