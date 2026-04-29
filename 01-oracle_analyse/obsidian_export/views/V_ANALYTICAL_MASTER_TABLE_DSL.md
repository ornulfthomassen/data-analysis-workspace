# V_ANALYTICAL_MASTER_TABLE_DSL

**Schema:** `CCM` | **Type:** `View`

## Description
This view, 'V_ANALYTICAL_MASTER_TABLE_DSL', serves as a consolidated analytical master table specifically for Digital Subscriber Line (DSL) subscriptions. It aggregates monthly historical data from various administrative and dimension tables, including subscription history, customer information, detailed subscription characteristics, DSL-specific details, and aggregated subscription statistics. The view enriches the data with derived keys for current and next month periods, and calculates various metrics related to subscription activity, product attributes, voice traffic, and revenue. It filters out certain customer types and statuses, and explicitly excludes known test customer IDs, preparing a clean dataset for analytical reporting focused on DSL services.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| PERIOD_MONTH_KEY_CHAR |
| LAST_DATE |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| CUSTOMER_SK_OWNER |
| CUSTOMER_SK_USER |
| PRODUCT_BRAND |
| SUBS_NO_DAYS_ACTIVE |
| PROD_NO_DAYS_ACTIVE |
| NO_DAYS_LAST_START |
| NO_DAYS_LAST_CHANGE |
| NO_DAYS_BIND_START |
| NO_DAYS_BIND_END |
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
| Column Name |
|---|
| CUSTOMER_SK |
| PERIOD_MONTH_KEY |
| CUSTOMER_TYPE_CD |
| CUSTOMER_STATUS_CD |
- ← [[CLM_ADM.ADM_SUBSCR_DETAIL_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PERIOD_MONTH_KEY |
| SUBS_TYPE |
| BINDING_ACTIVE |
| PRODUCT_ID |
| FRIFAM_NO_DAYS_ACTIVE |
| MIN_SKY_NO_DAYS_ACTIVE |
- ← [[CLM_ADM.ADM_DSL_SUBSCR_DETAIL_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PERIOD_MONTH_KEY |
| NO_DAYS_ACTIVE |
| BINDING_END_DATE |
| PRODUCT_OFFER_ID |
| PRODUCT_OFFER_DESC |
| DRM_PRODUCT_GROUP |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_SERVICE |
| SOURCE_PRODUCT_ID_1 |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_AGG]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PERIOD_MONTH_KEY |
| NUMBER_SPEECH_NORGE_PREV1 |
| NUMBER_SPEECH_NORGE_PREV2 |
| NUMBER_SPEECH_NORGE_PREV3 |
| NUMBER_SPEECH_UTLAND_PREV1 |
| NUMBER_SPEECH_UTLAND_PREV2 |
| NUMBER_SPEECH_UTLAND_PREV3 |
| DURAT_SPEECH_NORGE_PREV1 |
| DURAT_SPEECH_NORGE_PREV2 |
| DURAT_SPEECH_NORGE_PREV3 |
| DURAT_SPEECH_UTLAND_PREV1 |
| DURAT_SPEECH_UTLAND_PREV2 |
| DURAT_SPEECH_UTLAND_PREV3 |
| KR_SPEECH_NORGE_PREV1 |
| KR_SPEECH_NORGE_PREV2 |
| KR_SPEECH_NORGE_PREV3 |
| KR_SPEECH_UTLAND_PREV1 |
| KR_SPEECH_UTLAND_PREV2 |
| KR_SPEECH_UTLAND_PREV3 |
| GROSS_PERIODIC_FEE_FULL |
| NET_FEE |
| NET_USE |
| NET_PERIODIC_FEE |
| NET_DISCOUNT_PERIODIC_FEE |
| NET_INITIATION_FEE |
| NET_TERMINATION_FEE |
| NET_DISCOUNT_FIXED_FEE |
| NET_DISCOUNT_STARTUP_FEE |
| NET_AMOUNT_USE |
| NET_DISCOUNT_AMOUNT_USE |

