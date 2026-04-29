# P_ADM_TVILLING_ESIM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure calculates daily aggregated statistics related to 'TALETVILLING' (twin talk/eSIM) products. It identifies eSIMs associated with subscriptions, categorizes them by market (BUSINESS/CONSUMER) and product, and then counts their volume. The aggregated results (DAY, MARKET, PRODUCT_NAME, VOLUME) are then inserted as a new partition into the permanent table `ADM_TVILLING_ESIM`. The procedure handles the creation of the daily partition and checks for existing data to prevent accidental overwrites.

## Data Sources (Inputs)
- ← [[ADM_TVILLING_ESIM]]
- ← [[CLM_CCM.ODS_SUBSCRIPTION_MV]]
| Column Name |
|---|
| MAIN_NUMBER |
| MARKET_AREA_ID |
| PRODUCT_OFFER_ID |
| SUBSCRIPTION_ID |
- ← [[CLM_CCM.ODS_SUBSCRIBED_OFFER_MV]]
| Column Name |
|---|
| SUB_NUMBER |
| SUBSCRIPTION_ID |
| PRODUCT_OFFER_ID |
- ← [[CRM_ANALYSE.PD]]
| Column Name |
|---|
| PRODUCT_NAME |
| PRODUCT_KEY |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_MARKET_PRODUCT |
- ← [[SIMNR.SIMCARD_MSISDN_USAGE_STG]]
| Column Name |
|---|
| MSISDN_ID |
| ICC_ID |
| START_DATE |
| END_DATE |
- ← [[SIMNR.SIMCARD_STG]]
| Column Name |
|---|
| ICC_ID |
| IMSI_NUMBER |
| IMSI_INTERVAL_ID |
| SIMCARD_TYPE_ID |
- ← [[SIMNR.SIMCARD_TYPE_STG]]
| Column Name |
|---|
| SIMCARD_TYPE_ID |
| SIMCARD_TYPE_DESCR |
| IMSI_INTERVAL_TYPE_ID |
| SIMCARD_FORM_FACTOR_ID |
- ← [[SIMNR.IMSI_INTERVAL_TYPE_STG]]
| Column Name |
|---|
| IMSI_INTERVAL_TYPE_DESCR |
| IMSI_INTERVAL_TYPE_ID |
- ← [[SIMNR.SIMCARD_FORM_FACTOR_STG]]
| Column Name |
|---|
| SIMCARD_FORM_FACTOR_ID |

## Target Tables (Outputs)
- → [[TMP1_TVILLING_ESIM]]
| Column Name |
|---|
| MAIN_NUMBER |
| SUB_NUMBER |
| MARKET |
| PRODUCT_OFFER_ID |
| PRODUCT_NAME |
- → [[TMP2_TVILLING_ESIM]]
| Column Name |
|---|
| SUB_NUMBER |
| MAIN_NUMBER |
| MARKET |
| PRODUCT_OFFER_ID |
| PRODUCT_NAME |
| ICC_ID |
| IMSI_NUMBER |
| IMSI_INTERVAL_ID |
| CTRL_IMSI_INTV_ID |
| START_DATE |
| END_DATE |
| IMSI_INTERVAL_TYPE_DESCR |
| SIMCARD_TYPE_DESCR |
- → [[TMP3_TVILLING_ESIM]]
| Column Name |
|---|
| DAY |
| MARKET |
| PRODUCT_NAME |
| VOLUME |
- → [[ADM_TVILLING_ESIM]]
| Column Name |
|---|
| DAY |
| MARKET |
| PRODUCT_NAME |
| VOLUME |

