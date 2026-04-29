# MOBILE_REP_SERVICEORDERS_MV

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive reporting dataset for analyzing mobile service orders. It calculates various Key Performance Indicators (KPIs) related to product changes, new sales (including speech-specific and offer-specific new sales), porting out, terminations, and new/removed device swaps. It enriches the service order details with product information (current and previous), dealer details, service provider data, device (IMEI) information, and customer add-on features (goodies). The view also derives time-based attributes and categorizes sales into a 'Sales Matrix' based on product rank and brand changes.

## Data Sources (Inputs)
- ← [[ONL_REP.SERVICE_ORDER]]
| Column Name |
|---|
| ORDER_ID |
| ORDER_ARRIVAL_DATE |
| ORDER_STATUS_ID |
| ORDER_ACTION_TYPE_ID |
| CUST_TYPE_ID |
| ORDER_PROCESSED_DATE |
| DEALER_ID |
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
| Column Name |
|---|
| ORDER_ID |
| PRODUCT_STATUS_ID |
| PRODUCT_ACTION_TYPE_ID |
| SUBSCR_ID |
| PRODUCT_ID |
| ORDER_PHONE_NUM |
| ORDER_LINE_ID |
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT_PARAM]]
| Column Name |
|---|
| ORDER_ID |
| PARAM_ID |
| PARAM_STATUS_ID |
| PARAM_VALUE |
- ← [[ONL_REP.SUBSCRIBED_OFFER_PARAM_ORDER]]
| Column Name |
|---|
| ORDER_ID |
| PARAM_ID |
| PARAM_CATEGORY_ID |
| ACTION_TYPE_ID |
| PARAM_VALUE |
- ← [[ONL_REP.SUBSCRIBED_OFFER_ORDER]]
| Column Name |
|---|
| ORDER_ID |
| PRODUCT_OFFER_ID |
| ACTION_TYPE_ID |
| STATUS_ID |
| CREATED_DATE |
| PRODUCT_OFFER_CATEGORY_ID |
| PRODUCT_ORDER_LINE_ID |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| SOURCE_PRODUCT_ID_1 |
| PRODUCT_FAMILY_NAME |
| SOURCE_SYSTEM_NAME |
| PRODUCT_DESC |
| DRM_PRODUCT_GROUP |
| PRODUCT_NAME |
| PRODUCT_BRAND |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_PRODUCT_CATEGORY |
| PRIMARY_PRODUCT_FLAG |
| DRM_COMMON_PORTFOLIO |
| TK_PRODUCT_RANK |
| DRM_COMMON_BRAND |
| MONTHLY_PRICE |
- ← [[CM.SUBSCRIPTION_OFFER_INCENTIVE]]
| Column Name |
|---|
| SUBSCR_ID |
| INC_VALID_FROM_DATE |
| INC_VALID_TO_DATE |
| STATUS |
| PARAMETER_ID |
| PRODUCT_OFFER_ID |
- ← [[CCDW.SERVICE_PROVIDER]]
| Column Name |
|---|
| SERVICE_PROVIDER_ID |
| SERVICE_PROVIDER_NAME |
- ← [[CLM_CCM.V_CCM_DEALER_DIM]]
| Column Name |
|---|
| SOURCE_DEALER_ID |
| SALES_CHANNEL |
| DEALER_NAME |
| DEALER_CHAIN_NAME |
| DRM_SALES_CHANNEL_GEN01_DESC |
| DRM_SALES_CHANNEL_GEN02_DESC |
| DRM_SALES_CHANNEL_GEN03_DESC |
| DRM_SALES_CHANNEL_GEN04_DESC |
| DRM_SALES_CHANNEL_GEN05_DESC |
| DRM_SALES_CHANNEL_GEN06_DESC |
| DRM_SALES_CHANNEL_GEN07_DESC |
| DRM_RETAIL_GROUP |
- ← [[GALAXY.HANDSET_DIM_V]]
| Column Name |
|---|
| HANDSET_KEY |
| MANUFACTURER |
| MARKETING_NAME |
- ← [[CLM_KIM.V_REALTIME_GOODIES]]
| Column Name |
|---|
| SUBSCR_ID |
| BILDEPRINT |
| DATA_SWITCH |
| DATABOOST |
| EKSTRA_SIM |
| FERIEDATA |
| GADGETS |
| HOLD_NORGE_RENT |
| LADEAVTALE |
| RING_UTLAND |
| ROAM_I_VERDEN |
| SE_HVEM |
| TOTAL_GOODIES |
| TVILLING_SIM |
| VG_PLUSS |

