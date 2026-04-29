# ADM_SWAP_FLAGGING

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view consolidates detailed information for 'SWAP' agreements. It identifies active 'SWAP' products associated with agreements, extracts IMEI details from product configurations, and links these to original subscription main numbers and usage-based main numbers and subscriber IDs. It then prioritizes the latest IMEI usage data for each agreement to provide a comprehensive, current view of swap-related agreements, their owners, users, and IMEI history.

## Data Sources (Inputs)
- ← [[CCDW.AGREEMENT]]
| Column Name |
|---|
| AGREEMENT_ID |
| AGREEMENT_OWNER_ID |
| START_DATE |
| END_DATE |
| BUSINESS_AREA_ID |
- ← [[CCDW.AGREEMENT_PRODUCT_CONFIG]]
| Column Name |
|---|
| AGREEMENT_ID |
| CURRENT_STATUS |
| CONFIG_PARAMETER_ID |
| PRODUCT_OFFER_ID |
| CONFIG_PARAMETER_VALUE |
| START_DATE |
| END_DATE |
| SOURCE_AGREEMENT_ID |
| SOURCE_AGREEMENT_OFFER_ID |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME |
| DRM_COMMON_MARKET_PRODUCT |
| PRODUCT_CATEGORY_ID |
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]
| Column Name |
|---|
| SUBSCR_ID |
| PARAMETER_VALUE |
| PARAMETER_ID |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |
| SUBSCRIPTION_ID |
- ← [[CRM_ANALYSE.ADM_MOBIL_SUBSCR_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| SUBSCR_ID_NUM |
| LAST_USER |
- ← [[LIVE.EUREKA_IMEI]]
| Column Name |
|---|
| IMEI |
| TERMINAL_USE_FIRST_DATE |
| TERMINAL_USE_LAST_DATE |
| DIRECTORY_NUMBER_ID |
| SUBSCR_ID |

