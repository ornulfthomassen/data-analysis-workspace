# P_ADM_TVILLING_ESIM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure processes daily 'twin eSIM' subscription and usage data. It joins subscription details with product information to identify relevant 'twin SIM-card' offerings, then enriches this with SIM card technical details (ICC_ID, IMSI, SIM card type, etc.) specifically for eSIMs. Finally, it aggregates the volume of these 'twin eSIM' services by market and product name for the current day and loads these aggregated statistics into a daily partition of the permanent target table ADM_TVILLING_ESIM.

## Data Sources (Inputs)
- ← [[CLM_CCM.ODS_SUBSCRIPTION_MV]]
- ← [[CLM_CCM.ODS_SUBSCRIBED_OFFER_MV]]
- ← [[CRM_ANALYSE.PD]]
- ← [[SIMNR.SIMCARD_MSISDN_USAGE_STG]]
- ← [[SIMNR.SIMCARD_STG]]
- ← [[SIMNR.SIMCARD_TYPE_STG]]
- ← [[SIMNR.IMSI_INTERVAL_TYPE_STG]]
- ← [[SIMNR.SIMCARD_FORM_FACTOR_STG]]

## Target Tables (Outputs)
- → [[ADM_TVILLING_ESIM]]
- → [[TMP1_TVILLING_ESIM]]
- → [[TMP2_TVILLING_ESIM]]
- → [[TMP3_TVILLING_ESIM]]

