# VYA_CCM_SUBS_EQUIPMENT_INFO

**Schema:** `CCM` | **Type:** `View`

## Description
This view, VYA_CCM_SUBS_EQUIPMENT_INFO, provides a comprehensive overview of subscriber equipment details. It combines information related to SIM cards (ICC ID, IMSI, network support, form factor), devices (TAC, IMEI, model, manufacturer, color, memory), and associated agreements such as insurance and swap products, including their validity periods. It also integrates device range and historical first period month key data from administrative dimensions, presenting a unified view of subscriber and device-related contractual information.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_SUBS_EQUIPMENT_INFO_V]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SIM_ICC_ID |
| SIM_IMSI_NUMBER |
| SIM_NETTWORK_SUPPORTED |
| SIM_FORM_FACTOR_NAME |
| SIM_ESIM_TYPE_NAME |
| DEVICE_TAC_NUM |
| DEVICE_IMEI |
| DEVICE_IMEI_FULL |
| DEVICE_MODEL_ID |
| DEVICE_MODEL_NAME |
| DEVICE_USE_FIRST_DATE |
| DEVICE_USE_LAST_DATE |
| DEVICE_COLOR_NAME |
| DEVICE_MEMORY |
| AGRM_ROOT_AGREEMENT_KEY |
| AGRM_ROOT_SOURCE_AGREEMENT_ID |
| AGRM_INSURANCE_PRODUCT_KEY |
| AGRM_INSURANCE_PRODUCT_NAME |
| AGRM_INSURANCE_VALID_FROM_DATE |
| AGRM_INSURANCE_VALID_TO_DATE |
| AGRM_INS_CAMP_PRODUCT_KEY |
| AGRM_INS_CAMP_PRODUCT_NAME |
| AGRM_INS_CAMP_VALID_FROM_DATE |
| AGRM_INS_CAMP_VALID_TO_DATE |
| AGRM_SWAP_PRODUCT_KEY |
| AGRM_SWAP_PRODUCT_NAME |
| AGRM_SWAP_VALID_FROM_DATE |
| AGRM_SWAP_VALID_TO_DATE |
- ← [[CLM_CCM.CCM_HANDSET_DIM_V]]
| Column Name |
|---|
| DEVICE_KEY |
| DEVICE_MANUFACTURER |
| DEVICE_MARKETING_NAME |
| DEVICE_TECHNOLOGY_CLASS |
| DEVICE_TYPE |
| LOCAL_SALES_START_DTTM |
- ← [[CLM_ADM.ADM_DEVICE_RANGE_DIM]]
| Column Name |
|---|
| DEVICE_KEY |
| DEVICE_RANGE |
| MODEL_ID |
- ← [[CLM_ADM.ADM_HANDSET_HIST_AGG]]
| Column Name |
|---|
| MODEL_KEY |
| FIRST_PERIOD_MONTH_KEY |

