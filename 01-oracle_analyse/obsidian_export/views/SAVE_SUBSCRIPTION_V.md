# SAVE_SUBSCRIPTION_V

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a comprehensive view of churn prevention (saved) cases, linking them to customer accounts, associated subscriptions (TV, broadband), and their respective product categories. It details case attributes like solution, dates, descriptions, origin, main/sub groups, cancellation period, channel, competitor, product, and various termination/saved reasons. It also identifies the 'VALUECHAIN' and calculates the number of TV and broadband subscriptions per case/account/subscriber number, along with subscriber-level customer and location keys.

## Data Sources (Inputs)
- ← [[CVIEW_STAGING."CASE"]]
| Column Name |
|---|
| CASENUMBER |
| ACCOUNTID |
| CREATEDDATE |
| SAVE_PRODUCT__C |
| ADDRESS_SUBSCRIPTION_ID__C |
| ISDELETED |
| CASE_SOLUTION__C |
| CLOSEDDATE |
| DESCRIPTION |
| HOVEDGRUPPE_MANUELL__C |
| ORIGIN |
| UNDERGRUPPE_1_MANUELL__C |
| UNDERGRUPPE_2_MANUELL__C |
| SAVE_CANCELLATION_PERIOD__C |
| SAVE_CHANNEL__C |
| SAVE_COMPETITOR__C |
| SAVE_REASON_FOR_SAVED__C |
| SAVE_REASON_FOR_TERMINATION__C |
| SAVE_SAVED__C |
| A_NUMBER__C |
| CHANNEL_SUBCATEGORY__C |
| TERMINATION_SUBCATEGORY__C |
| TERMINATION_SUBCATEGORY_TV__C |
| TERMINATION_FROM_CHANNEL__C |
- ← [[CVIEW_STAGING.ADDRESS__C]]
| Column Name |
|---|
| ACCOUNTID__C |
| SUBSCRIPTIONID__C |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SOURCE_SYSTEM_KEY |
| SUBSCRIPTION_ID |
- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| START_DATE |
| END_DATE |
| PRODUCT_CATEGORY_ID |
- ← [[CCDW.PRODUCT_CATEGORY]]
| Column Name |
|---|
| PRODUCT_CATEGORY_NAME |
| PRODUCT_CATEGORY_ID |
- ← [[KAS.KUNDE]]
| Column Name |
|---|
| ABONNENT_NR |
| ANSVARSTED |
- ← [[KAS.ABONNENTNR_MSISDN]]
| Column Name |
|---|
| ABONNENT_NR |
- ← [[GALAXY.SUBSCRIPTION_DIM]]
| Column Name |
|---|
| SUBSCRIPTION_KEY |
| OWNER_CUSTOMER_KEY |
| SUBSCR_USER_LOC_KEY |
- ← [[CVIEW_STAGING.ACCOUNT]]
| Column Name |
|---|
| ID |
| CUSTOMER_GROUP__C |

