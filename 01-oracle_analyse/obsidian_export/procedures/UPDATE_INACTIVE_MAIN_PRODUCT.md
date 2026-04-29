# UPDATE_INACTIVE_MAIN_PRODUCT

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This procedure updates and deletes subscription main product information based on data discrepancies and subscription lifecycle status. It identifies subscriptions with incorrect main product IDs and updates them. It also identifies inactive subscriptions in the source system (CM.SUBSCRIPTION) and deletes them from the local CCM_SUBSCRIPTION and related campaign offer tables. All update and delete actions are logged in a dedicated tracking table (LOG_SUBSCRIPTION_MAIN_PROD_UPD). Finally, it maintains an 'exclude' list (EXCLUDE_FROM_AST) for analytics or reporting by populating it with SUBSCRIPTION_IDs of processed subscriptions from the tracking log for the current day.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
- ← [[CCM_SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| MAIN_PRODUCT_ID |
| MAIN_PRODUCT_START_DATE |
| LOAD_DTTM |
| SOURCE_SYSTEM_SUBSCR_ID_1 |
- ← [[CCM_PRODUCT_TYPE_CONFIG]]
| Column Name |
|---|
| ID |
| PARENT |
| PRODUCT_NAME |
| PRODUCT_FAMILY_NAME |
| VALUE |
- ← [[CM.SUBSCRIPTION_OFFER_INCENTIVE]]
| Column Name |
|---|
| SUBSCR_ID |
| PRODUCT_OFFER_ID |
| INFO_IS_DELETED |
| INC_VALID_TO_DATE |
- ← [[RTDM_CCM_SUBSCR_CAMP_OFFER_NEW]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
- ← [[CM.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCR_ID |
| INFO_IS_DELETED |
| SUBSCR_VALID_TO_DATE |
- ← [[LOG_SUBSCRIPTION_MAIN_PROD_UPD]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| RIKTIG_START_DATE |

## Target Tables (Outputs)
- → [[LOG_SUBSCRIPTION_MAIN_PROD_UPD]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| FEIL_PRODUCT_ID |
| FEIL_START_DATE |
| FEIL_PRODUCT_NAVN |
| FEIL_PRODUCT_FAMILIE |
| OLD_LOAD_DTTM |
| RIKTIG_PRODUCT_ID |
| RIKTIG_START_DATE |
| RIKTIG_PRODUCT_NAVN |
| RIKTIG_PRODUCT_FAMILIE |
| UPDATE_DTTM |
| RADER_OPPDATERT |
- → [[CCM_SUBSCRIPTION]]
| Column Name |
|---|
| MAIN_PRODUCT_ID |
| MAIN_PRODUCT_START_DATE |
| LOAD_DTTM |
- → [[RTDM_CCM_SUBSCR_CAMP_OFFER_NEW]]
- → [[TMP_EXCLUDE_FROM_AST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
- → [[EXCLUDE_FROM_AST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |

