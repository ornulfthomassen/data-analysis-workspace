# V_FAMILIEBONUS_HIST_RAW

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
The view 'V_FAMILIEBONUS_HIST_RAW' retrieves historical raw data for 'Familiebonus' (family bonus) agreements, specifically for product offer ID 956. It combines agreement, offer, and configuration details, including parameter values related to data volume and service types. It calculates the data volume in an agreement (MB_IN_AGR) and a family bonus basis (FB_GRUNNLAG), and identifies the presence of specific service types like Mobile, Business, SWAP, Fixed Telephony, and Fixed Broadband based on configuration parameters. This view provides a comprehensive, raw dataset for analyzing specific family bonus agreements.

## Data Sources (Inputs)
- ← [[CM.AGREEMENT_OFFER]]
| Column Name |
|---|
| AGREEMENT_ID |
| VALID_FROM_DATE |
| VALID_TO_DATE |
| AGREEMENT_OFFER_ID |
| MARKET_NAME |
| PRODUCT_OFFER_ID |
- ← [[CM.AGREEMENT_OFFER_COMPONENT]]
| Column Name |
|---|
| AGREEMENT_OFFER_ID |
| AGREEMENT_COMPONENT_ID |
- ← [[CCDW.AGREEMENT_MAPPING]]
| Column Name |
|---|
| AGREEMENT_ID |
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |
- ← [[CM.AGREEMENT_OFFER_CONFIGURATION]]
| Column Name |
|---|
| AGREEMENT_COMPONENT_ID |
| PARAMETER_ID |
| PARAMETER_VALUE |
| VALID_FROM_DATE |
| VALID_TO_DATE |
- ← [[ONL_REP.SUBSCRIBED_OFFER_PARAM_ORDER]]
| Column Name |
|---|
| PARAM_VALUE |
| PARAM_ID |
| OFFER_ORDER_LINE_ID |
| ORDER_ID |
| PARAM_ORDER_LINE_ID |
- ← [[ONL_REP.SUBSCRIBED_OFFER_ORDER]]
| Column Name |
|---|
| OFFER_ORDER_LINE_ID |
| ORDER_ID |
| PRODUCT_OFFER_CATEGORY_ID |
| ACTION_TYPE_ID |
| CREATED_DATE |
| PRODUCT_OFFER_ID |
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
| Column Name |
|---|
| ORDER_LINE_ID |
| ORDER_ID |
| SUBSCR_ID |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| SOURCE_PRODUCT_ID_1 |
| SOURCE_SYSTEM_NAME |
| PRODUCT_NAME |
| PRODUCT_KEY |

