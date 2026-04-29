# OS

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates mobile subscription and product offer details from ODS tables, enriching them with product information. It identifies various customer roles (owner, payer, user) associated with subscriptions and presents key subscription and product attributes, grouped by product name, subscription ID, and main number.

## Data Sources (Inputs)
- ← [[ODS.SUBSCRIPTION_ODS_MOB]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PRODUCT_OFFER_ID |
| SUBSCR_START_DATE |
| MARKET_AREA_ID |
| CUSTOMER_ROLE_ID |
| CUSTOMER_ID |
| SECRET_NUMBER |
| RECORD_CHANGE_DATE |
- ← [[ODS.SUBSCRIBED_OFFER_ODS_MOB]]
| Column Name |
|---|
| PRODUCT_OFFER_ID |
| SRC_PRODUCT_ID |
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| START_DATE |
| SRC_PRODUCT_CATEGORY_ID |
- ← [[PD]]
| Column Name |
|---|
| PRODUCT_NAME |
| PRODUCT_KEY |

