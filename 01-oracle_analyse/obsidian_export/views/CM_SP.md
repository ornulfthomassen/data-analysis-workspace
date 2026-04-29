# CM_SP

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view combines subscription details with associated offer incentives and product offer information. It filters for product offers belonging to category ID 20 and provides a distinct list of records, ordered by subscription validity dates. The view essentially links customer subscriptions to specific product offers and their incentive details.

## Data Sources (Inputs)
- ← [[CM.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCR_ID |
| CUST_ID_PAYER |
| CUST_ID_RESP |
| CUST_ID_USER |
| DIRECTORY_NUMBER_ID |
| SUBSCR_VALID_FROM_DATE |
| SUBSCR_VALID_TO_DATE |
- ← [[CM.SUBSCRIPTION_OFFER_INCENTIVE]]
| Column Name |
|---|
| SUBSCR_ID |
| INC_VALID_FROM_DATE |
| INC_VALID_TO_DATE |
| INFO_CHG_DATE |
| PARAMETER_ID |
| PRODUCT_OFFER_ID |
- ← [[PCAT.PRODUCT_OFFER]]
| Column Name |
|---|
| PRODUCT_OFFER_ID |
| PRODUCT_OFFER_CATEGORY_ID |
| PUBLIC_NAME |

