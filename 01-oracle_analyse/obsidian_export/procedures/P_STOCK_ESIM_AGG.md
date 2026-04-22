# P_STOCK_ESIM_AGG

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Aggregates and analyzes eSIM (embedded SIM) related data, including twin cards ('tilleggskort') and main subscriptions ('hovedabonnementer'), along with their associated device information. The procedure identifies and categorizes active eSIM connections, their linked main/twin numbers, and the devices used (manufacturer, marketing name, model, type). It calculates device rankings and summarizes this information daily into two partitioned target tables: one for device-specific eSIM statistics (STOCK_ESIM_DEVICE) and another for main product aggregation related to twin/extra cards with eSIMs (STOCK_ESIM_TWIN). The process involves multiple steps of data extraction, transformation, and aggregation using several intermediate temporary tables.

## Data Sources (Inputs)
- ← [[CLM_CCM.ODS_SUBSCRIPTION_MV]]
- ← [[CLM_CCM.ODS_SUBSCRIBED_OFFER_MV]]
- ← [[CRM_ANALYSE.PD]]
- ← [[SIMNR.SIMCARD_MSISDN_USAGE_STG]]
- ← [[SIMNR.SIMCARD_STG]]
- ← [[SIMNR.SIMCARD_TYPE_STG]]
- ← [[SIMNR.IMSI_INTERVAL_TYPE_STG]]
- ← [[SIMNR.SIMCARD_FORM_FACTOR_STG]]
- ← [[LIVE.EUREKA_IMEI]]
- ← [[CLM_ADM.ADM_GSMA_MARKETING_NAME_DIM]]
- ← [[GALAXY.HANDSET_DIM_V]]

## Target Tables (Outputs)
- → [[TMP1_XTRACARDS]]
- → [[TMP2_XTRACARDS_ESIM]]
- → [[TMP3_MAINSUB_PRODUCTS]]
- → [[TMP4_XTRACARDS_DEVICE]]
- → [[TMP5_MAINSUB_ESIM]]
- → [[TMP6_MAINSUB_DEVICE]]
- → [[TMP7_DEVICE_ESIM]]
- → [[TMP8_MAIN_PRODUCT_AGG]]
- → [[STOCK_ESIM_DEVICE]]
- → [[STOCK_ESIM_TWIN]]

