# TV_PROGRAMKOST_V

**Schema:** `CCM` | **Type:** `View`

## Description
Combines TV content inventory, usage, and cost data with content product details to provide a comprehensive view of TV program economics.

## Data Sources (Inputs)
- ← [[CCM.TV_CONTENT_IB_UB_V]]
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
| UB |
| IB |
- ← [[QLIKVIEW.TV_CONTENT_PRODUCT_V]]
| Column Name |
|---|
| PRODUCT_NR |
| CONTENT_ID |
| CONTENT_NAME |
| SEGMENT |
| CONTENT_GRP |
| VENDOR |
| PACKAGE_GRP |

