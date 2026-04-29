# P_ADM_DEVICE_RANGE_DIM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure (`P_ADM_DEVICE_RANGE_DIM`) is designed to populate and maintain a device range dimension table (`CLM_ADM.ADM_DEVICE_RANGE_DIM`). It categorizes devices (e.g., 'High-End', 'Mid-Range', 'Rugged') based on marketing names and manufacturers, calculates the maximum number of terminals for each device, and consolidates marketing name variants for device models. It involves inserting new device entries and then performing several updates to refine device attributes based on current usage data and existing marketing information.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| END_DATE |
| BUSINESS_AREA_ID |
- ← [[CCDW.SUBSCRIPTION_HANDSET]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| TAC_ID |
| IMEI |
- ← [[CCDW.HANDSET_TYPE_EXT]]
| Column Name |
|---|
| TACFAC |
| HAT_PRODUCER |
| MODELID |
- ← [[CLM_ADM.ADM_GSMA_MARKETING_NAME_DIM]]
| Column Name |
|---|
| TAC |
| MARKETING_NAME_L1 |
| MODEL_ID |
- ← [[CLM_ADM.ADM_DEVICE_RANGE_DIM]]
| Column Name |
|---|
| DEVICE_KEY |
| MODEL_ID |
| MODEL_MARKETING_NAME |
| MAX_NO_TERMINALS |
| NAVNEVARIANTER |
| LIST_MARKETING_NAME_L1 |
| DEVICE_RANGE |
- ← [[CLM_ADM.CURRENT_TERMINAL_USE]]
| Column Name |
|---|
| TAC_ID |
| ANTALL |

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_DEVICE_RANGE_DIM]]
| Column Name |
|---|
| DEVICE_KEY |
| MANUFACTURER |
| MODEL_ID |
| MODEL_MARKETING_NAME |
| DEVICE_RANGE |
| NAVNEVARIANTER |
| LIST_MARKETING_NAME_L1 |
| MAX_NO_TERMINALS |
| MAIN_MODEL_MARKETING_NAME |
| MAIN_DEVICE_RANGE |
- → [[CLM_ADM.CURRENT_TERMINAL_USE]]
| Column Name |
|---|
| TAC_ID |
| ANTALL |
- → [[CRM_ANALYSE.ADM_LOAD_HISTORY]]
| Column Name |
|---|
| OBJECT_NAME |
| PERIOD_DATE |
| STATUS |
| STATUS_MESSAGE |

