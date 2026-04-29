# VYA_ORDER_LINE_DETAIL_FACT_FT

**Schema:** `CCM` | **Type:** `View`

## Description
This view extracts historical order line detail for device insurance agreements that have been terminated after a fixed term of 2 or 5 years. It identifies these as 'Insurance Termination' events, calculating various keys and indicators for data warehousing purposes, primarily for analytics related to terminated agreements and associated products.

## Data Sources (Inputs)
- ← [[ODS.AGREEMENT_ODS_MOB]]
| Column Name |
|---|
| SRC_SERVICE_ORDER_ID |
| ORIGINAL_START_DATE |
| CUSTOMER_ID_OWNER |
| HANDSET_KEY |
| IMEI_FULL |
| SRC_ROOT_PRODUCT_ID |
| MSISDN_USER |
- ← [[ODS.AGREEMENT_OFFER_ODS_MOB]]
| Column Name |
|---|
| SRC_AGRM_AGREEMENT_OFFER_ID |
| END_DATE |
| INFO_CHG_DATE |
| PRODUCT_OFFER_ID |
| SRC_PROD_AGREEMENT_OFFER_ID |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_MARKET_PRODUCT |
| DRM_COMMON_REPORTING |
| PRODUCT_CATEGORY_ID |
- ← [[GALAXY.CUSTOMER_DIM]]
| Column Name |
|---|
| CUSTOMER_KEY |
| BIRTH_DATE_AGE |
| MAIN_ADDRESS_LOCATION_ID |
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
| Column Name |
|---|
| AGE_GROUP_KEY |
- ← [[GALAXY.SUBSCR_OWNER_LOC_DIM_V]]
| Column Name |
|---|
| SUBSCR_OWNER_LOC_KEY |
| SUBSCR_OWNER_POSTCODE_ID |
| SUBSCR_OWNER_MUNICIPAL_ID |
| SUBSCR_OWNER_MUNICIPAL |
| SUBSCR_OWNER_COUNTY_ID |
| SUBSCR_OWNER_COUNTY |
- ← [[GALAXY.DEALER_DIM]]
| Column Name |
|---|
| SOURCE_DEALER_ID |
| CURRENT_STATUS |
| DEALER_KEY |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| WEEK_NUMBER |
| RELATIVE_WEEK |
| MONTH_NUMBER |
| RELATIVE_MONTH |
| YEAR |
| YEAR_WEEK_NUMBER |
| YEAR_MONTH_NUMBER |
| YEAR_QUARTER_NUMBER |
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_KEY |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
| Column Name |
|---|
| MAIN_NUMBER |
| CURRENT_STATUS |
| SUBSCRIPTION_ID |
| LAST_PRODUCT_KEY |
| MARKET_AREA_ID |
- ← [[CCDW_ORDER.ORDER_MAPPING]]
| Column Name |
|---|
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |
| ORDER_ID |

