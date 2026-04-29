# RM_CCM_SUBS_EQUIPMENT_INFO

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a unified view providing comprehensive subscription and equipment information. This includes details about SIM cards (ICC ID, IMSI, network support, form factor, eSIM type), devices (TAC, IMEI, model, manufacturer, marketing name, technology class, type, color, memory, usage dates), and associated agreement details (offer IDs, product keys, end dates for swap and insurance agreements), all derived directly from the 'CLM_CCM.CCM_SUBS_EQUIPMENT_INFO_V' view.

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
| DEVICE_TAC |
| DEVICE_IMEI |
| DEVICE_MODEL_ID |
| DEVICE_MODEL_NAME |
| DEVICE_USE_FIRST_DATE |
| DEVICE_USE_LAST_DATE |
| DEVICE_AGRMT_OFFER_ID_SWAP |
| DEVICE_AGRMT_OFFER_ID |
| DEVICE_AGRMT_PRODUCT_KEY_SWAP |
| DEVICE_AGRMT_END_DATE_SWAP |
| DEVICE_AGRMT_PRODUCT_KEY_INSR |
| DEVICE_AGRMT_END_DATE_INSR |
| DEVICE_MANUFACTURER |
| DEVICE_MANUFACTURER_SHORT |
| DEVICE_MARKETING_NAME |
| DEVICE_TECHNOLOGY_CLASS |
| DEVICE_TYPE |
| DEVICE_COLOR_NAME |
| DEVICE_MEMORY |
| AGRM_DEVICE_IMEI |
| AGRM_ROOT_AGREEMENT_KEY |
| AGRM_ROOT_SOURCE_AGREEMENT_ID |
| AGRM_INSURANCE_PRODUCT_KEY |
| AGRM_INSURANCE_PRODUCT_NAME |
| AGRM_INSURANCE_VALID_FROM_DATE |
| AGRM_INSURANCE_VALID_TO_DATE |
| AGRM_SWAP_PRODUCT_KEY |
| AGRM_SWAP_PRODUCT_NAME |
| AGRM_SWAP_VALID_FROM_DATE |
| AGRM_SWAP_VALID_TO_DATE |
| AGRM_SWAP_MONTHS_TO_END_DATE |

