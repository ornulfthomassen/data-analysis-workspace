# V_MOB_SUBSCR

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a comprehensive view of active mobile subscriptions, integrating details such as product name, subscription type, key identifiers, market area, start/end dates, and associated binding contract information, derived from a combination of subscription, product, and product configuration data.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| PRODUCT_OFFER_ID |
| KURT_ID_OWNER |
| KURT_ID_USER |
| KURT_ID_PAYER |
| MARKET_AREA_ID |
| INFO_CHG_DATE |
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PRODUCT_OFFER_ID |
| START_DATE |
| END_DATE |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME |
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
| Column Name |
|---|
| ID |
| PARENT |
| DESCRIPTION |

