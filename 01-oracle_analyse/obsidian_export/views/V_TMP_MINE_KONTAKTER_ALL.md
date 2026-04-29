# V_TMP_MINE_KONTAKTER_ALL

**Schema:** `CCM` | **Type:** `View`

## Description
Combines contact/user data with subscription, product, and customer details, calculating usage durations and providing a comprehensive view of user interactions and product subscriptions. It normalizes subscription and product type information by providing 'N/A' for missing values and calculates user age.

## Data Sources (Inputs)
- ← [[TMP_MINE_KONTAKTER_ALL]]
| Column Name |
|---|
| ID |
| USERID |
| STATE |
| CREATED_DTTM |
| LASTSYNCHRONIZED_DTTM |
| SUBSCRIPTION_ID |
- ← [[CLM_CCM.CCM_SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SUBSCRIPTION_TYPE |
| MAIN_PRODUCT_ID |
| USER_KURT_ID |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_FAMILY_NAME |
| PRODUCT_NAME |
- ← [[CLM_CCM.CCM_CUSTOMER]]
| Column Name |
|---|
| KURT_ID |
| AGE |

