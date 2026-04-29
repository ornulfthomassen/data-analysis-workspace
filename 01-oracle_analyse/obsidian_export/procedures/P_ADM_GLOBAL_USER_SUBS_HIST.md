# P_ADM_GLOBAL_USER_SUBS_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Generates and updates monthly user subscription history data for a specific year-month. It first creates a temporary table by joining various subscription, offer, and event data. This temporary table is then used to populate or refresh a partition within the main `ADM_GLOBAL_USER_SUBS_HIST` table via an exchange partition operation. The procedure also handles partition creation, error logging, and source data validation.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| LAST_DATE_KEY |
| LAST_DATE |
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]
| Column Name |
|---|
| SUBSCR_ID |
| PARAMETER_VALUE |
| VALID_FROM_DATE |
| VALID_TO_DATE |
| PARAMETER_ID |
- ← [[CM.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCR_ID |
| INFO_IS_DELETED |
| INFO_REG_DATE |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |
| SUBSCRIPTION_ID |
- ← [[COMOYO.COMOYO_SUB_GRANT_EVENTS]]
| Column Name |
|---|
| USER_ID |
| EVENT |
| SKUS |
| EVENT_TIME |
| LOAD_DATE |
| GRANTOR |
- ← [[GALAXY.SUBSCRIPTION_DIM_MV]]
| Column Name |
|---|
| PARENT_SUBSCRIPTION_KEY |
| COMOYO_USER_ID |
| SUBSCR_USER_START_DT_KEY |
| SUBSCR_CATEGORY_NAME |

## Target Tables (Outputs)
- → [[TMP_GLOBAL_USER_SUBS_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| COMOYO_USER_ID |
| FIRST_EVENT_DTTM |
| MIN_SKY_NO_DAYS_FIRST_USE |
- → [[ADM_GLOBAL_USER_SUBS_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| COMOYO_USER_ID |
| FIRST_EVENT_DTTM |
| MIN_SKY_NO_DAYS_FIRST_USE |

