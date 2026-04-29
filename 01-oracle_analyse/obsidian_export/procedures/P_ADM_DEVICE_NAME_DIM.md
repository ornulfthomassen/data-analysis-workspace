# P_ADM_DEVICE_NAME_DIM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Populates and updates a device marketing name dimension table (CLM_ADM.ADM_GSMA_MARKETING_NAME_DIM) by inserting new device records from a handset dimension view (CLM_ADM.ADM_HANDSET_DIM_V) and synchronizing model IDs with a terminal TAC table (CLM_CCM.CCM_TERMINAL_TAC). It inserts new records where the device TAC is not already present, updates original model IDs if null, and corrects model IDs based on the latest data from CCM_TERMINAL_TAC.

## Data Sources (Inputs)
- ← [[ADM_HANDSET_DIM_V]]
| Column Name |
|---|
| TAC_ID |
| HAT_MARKETING_NAME |
| MARKETING_NAME_L1 |
| MARKETING_NAME_L2 |
| MANUFACTURER |
| GSMA_DESIGNATION_TYPE |
| MODELID |
- ← [[ADM_GSMA_MARKETING_NAME_DIM]]
| Column Name |
|---|
| TAC |
| MODEL_ID |
| ORIGINAL_MODEL_ID |
- ← [[CCM_TERMINAL_TAC]]
| Column Name |
|---|
| MODELID |
| TACFACID |

## Target Tables (Outputs)
- → [[ADM_GSMA_MARKETING_NAME_DIM]]
| Column Name |
|---|
| TAC |
| ORIGINAL_MARKETING_NAME |
| MARKETING_NAME_L1 |
| MARKETING_NAME_L2 |
| MANUFACTURER |
| DESIGNATION_TYPE |
| CCM_TERMINAL_TAC_NAME |
| CCM_TERMINAL_TAC_DESCRIPTION |
| MODEL_ID |
| FAC |
| ORIGINAL_MODEL_ID |

