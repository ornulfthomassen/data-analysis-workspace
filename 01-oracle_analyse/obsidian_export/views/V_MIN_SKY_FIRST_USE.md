# V_MIN_SKY_FIRST_USE

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view identifies and consolidates the first recorded usage events for 'Min Sky' related services across different subscription types or data sources. It combines subscription details, customer identifiers, and event timestamps from various schemas to calculate the number of days since the initial event.

## Data Sources (Inputs)
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]
| Column Name |
|---|
| SUBSCR_ID |
| PARAMETER_VALUE |
| VALID_TO_DATE |
| PARAMETER_ID |
- ← [[CM.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCR_ID |
| DIRECTORY_NUMBER_ID |
| INFO_IS_DELETED |
| SUBSCR_VALID_TO_DATE |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |
| SUBSCRIPTION_ID |
- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| KURT_ID_OWNER |
| KURT_ID_USER |
| MARKET_AREA_ID |
| BUSINESS_AREA_ID |
| MAIN_NUMBER |
| PARENT_SUBSCRIPTION_ID |
| PRODUCT_OFFER_ID |
- ← [[COMOYO.COMOYO_SUB_GRANT_EVENTS]]
| Column Name |
|---|
| USER_ID |
| EVENT |
| SKUS |
| EVENT_TIME |
| LOAD_DATE |
- ← [[GALAXY.SUBSCRIPTION_DIM_MV]]
| Column Name |
|---|
| SUBSCRIPTION_KEY |
| COMOYO_USER_ID |

