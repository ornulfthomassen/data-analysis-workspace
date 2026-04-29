# VYA_CCM_SUBSCRIPTION

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates subscription details by joining the 'CCM_SUBSCRIPTION_V' table with 'ADM_CUSTOMER_MAPPING' to link subscriptions with their respective owner, user, and payer customer keys. It computes derived columns such as 'SUBSCRIPTION_KEY', 'CUSTOMER_SK_OWNER', 'CUSTOMER_SK_USER', 'CUSTOMER_SK_PAYER', and 'SUBS_DAYS_ACTIVE', providing a comprehensive, flattened view of subscription data.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_SUBSCRIPTION_V]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| OWNER_KURT_ID |
| USER_KURT_ID |
| PAYER_KURT_ID |
| MAIN_PRODUCT_ID |
| ORIGINAL_START_DATE |
| START_DATE |
| END_DATE |
| MAIN_PRODUCT_START_DATE |
| MAIN_PRODUCT_END_DATE |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |

