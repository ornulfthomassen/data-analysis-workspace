# P_ADM_SUBSCR_DETAIL_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure (`P_ADM_SUBSCR_DETAIL_HIST`) populates the `ADM_SUBSCR_DETAIL_HIST` table, which is partitioned by month (`YYYYMM`), with detailed subscription history data. It first performs data quality checks on several source tables. If checks pass, it creates a temporary table (`TMP_SUBSCR_DETAIL_HIST`), populates it with subscription data aggregated and joined from various source systems for the specified month. Finally, it uses an `EXCHANGE PARTITION` operation to efficiently load this data into the corresponding partition of the permanent `ADM_SUBSCR_DETAIL_HIST` table, handling partition creation, index rebuilding, and statistics computation.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| YEAR_MONTH_NUMBER |
| DAY |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_NAME |
| SOURCE_PRODUCT_ID_1 |
| SOURCE_SYSTEM_NAME |
| DRM_COMMON_PRODUCT_AREA |
| DRM_COMMON_PAYMENT |
| PRODUCT_PAYMENT_TYPE_NAME |
| PRODUCT_KEY |
| PRODUCT_NAME_USE |
| DRM_COMMON_MARKET_PRODUCT |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
| PRODUCT_CATEGORY_NAME |
- ← [[PCAT.PRODUCT_OFFER]]
| Column Name |
|---|
| PRODUCT_OFFER_ID |
| PRODUCT_OFFER_CATEGORY_ID |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| PRODUCT_OFFER_ID |
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
| Column Name |
|---|
| START_DATE |
| END_DATE |
| PRODUCT_OFFER_ID |
| SUBSCRIPTION_ID |
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| LAST_DATE |
| PERIOD_MONTH_KEY |

## Target Tables (Outputs)
- → [[TMP_SUBSCR_DETAIL_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| SUBS_CATEGORY |
| SUBS_TYPE |
| PRODUCT_ID |
| SOURCE_SYSTEM_KEY |
| PRODUCT_NAME |
| BANKID_USED_LAST1 |
| BANKID_USED_LAST2 |
| BANKID_USED_LAST3 |
| FRIFAM_NO_DAYS_ACTIVE |
| FORSIKRING_NO_DAYS_ACTIVE |
| MIN_SKY_NO_DAYS_ACTIVE |
| BINDING_NO_DAYS_ACTIVE |
| BINDING_ACTIVE |
| BINDING_PRODUCT_DESC |
| BINDING_TYPE |
| TERMINAL_BUNDELS |
| DATAKONTR_DOM_NO_DAYS_ACTIVE |
| DATAKONTR_ABR_NO_DAYS_ACTIVE |
| BINDING_PRODUCT_ID |
| BINDING_START_DATE |
| BINDING_END_DATE |
- → [[ADM_SUBSCR_DETAIL_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| SUBS_CATEGORY |
| SUBS_TYPE |
| PRODUCT_ID |
| SOURCE_SYSTEM_KEY |
| PRODUCT_NAME |
| BANKID_USED_LAST1 |
| BANKID_USED_LAST2 |
| BANKID_USED_LAST3 |
| FRIFAM_NO_DAYS_ACTIVE |
| FORSIKRING_NO_DAYS_ACTIVE |
| MIN_SKY_NO_DAYS_ACTIVE |
| BINDING_NO_DAYS_ACTIVE |
| BINDING_ACTIVE |
| BINDING_PRODUCT_DESC |
| BINDING_TYPE |
| TERMINAL_BUNDELS |
| DATAKONTR_DOM_NO_DAYS_ACTIVE |
| DATAKONTR_ABR_NO_DAYS_ACTIVE |
| BINDING_PRODUCT_ID |
| BINDING_START_DATE |
| BINDING_END_DATE |

