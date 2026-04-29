# ADM_AGREEMENTS_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view consolidates agreement-related data, specifically focusing on 'Swap Agreements' and 'Insurance Agreements'. It gathers comprehensive details such as agreement ownership, dealer information, start and end dates, product specifics (key, name, family), account details, unique agreement identifiers, invoice accounts, IMEI, device names, and IMEI status. The data is sourced from various operational and data warehousing tables, linking agreements to product configurations, subscriptions, and device information.

## Data Sources (Inputs)
- ← [[CCDW.AGREEMENT]]
| Column Name |
|---|
| AGREEMENT_OWNER_ID |
| DEALER_ID |
| START_DATE |
| END_DATE |
| ACCOUNT_ID |
| AGREEMENT_ID |
| BUSINESS_AREA_ID |
| AGREEMENT_OFFER_ID |
- ← [[CCDW.AGREEMENT_PRODUCT_CONFIG]]
| Column Name |
|---|
| AGREEMENT_ID |
| CURRENT_STATUS |
| CONFIG_PARAMETER_ID |
| PRODUCT_OFFER_ID |
| SOURCE_AGREEMENT_ID |
| CONFIG_PARAMETER_VALUE |
| START_DATE |
| END_DATE |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME |
| DRM_COMMON_MARKET_PRODUCT |
| PRODUCT_PORTFOLIO_NAME |
| PRODUCT_CATEGORY_ID |
| DRM_COMMON_PRODUCT_GROUP |
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]
| Column Name |
|---|
| SUBSCR_ID |
| PARAMETER_VALUE |
| PARAMETER_ID |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SOURCE_SYSTEM_KEY |
- ← [[AGR.EQUIPMENT]]
| Column Name |
|---|
| MARKETING_NAME |
| TAC |
- ← [[GALAXY.HANDSET_DIM_V]]
| Column Name |
|---|
| MARKETING_NAME |
| HANDSET_KEY |

