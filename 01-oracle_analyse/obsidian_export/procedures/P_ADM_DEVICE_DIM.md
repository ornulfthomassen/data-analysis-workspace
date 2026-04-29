# P_ADM_DEVICE_DIM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Reconstructs the CLM_ADM.ADM_DEVICE_DIM dimension table daily. It extracts and transforms handset data from GALAXY.HANDSET_DIM_V and CLM_ADM.ADM_GSMA_MARKETING_NAME_DIM, enriching it with various device attributes and classifications. The process involves creating a temporary table, populating it, and then atomically replacing the existing ADM_DEVICE_DIM table via a rename operation. Finally, it creates a unique index and primary key constraint on the newly replaced table and updates load history.

## Data Sources (Inputs)
- ← [[GALAXY.HANDSET_DIM_V]]
| Column Name |
|---|
| HANDSET_KEY |
| MANUFACTURER |
| MARKETING_NAME |
| CAMERA_INFO |
| HANDSET_TYPE |
| IS_5G |
| VOLTE_ACTIVATED |
| VOLTE_FLAG |
| LTE |
| UMTS |
| HSDPA |
| GPRS |
| EDGE |
| OS_INFO |
| LOCAL_SALES_START_DATE |
- ← [[CLM_ADM.ADM_GSMA_MARKETING_NAME_DIM]]
| Column Name |
|---|
| MARKETING_NAME_L1 |
| TAC |
- ← [[CLM_ADM.TMP_DEVICE_DIM]]
- ← [[CLM_ADM.ADM_DEVICE_DIM]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_DEVICE_DIM]]
| Column Name |
|---|
| DEVICE_KEY |
| LOAD_DATE_KEY |
| DEVICE_MANUFACTURER_SHORT |
| DEVICE_MARKETING_NAME |
| DEVICE_CAMERA_INFO |
| DEVICE_TYPE |
| DEVICE_CATEGORY |
| DEVICE_CLASS |
| DEVICE_OS_INFO |
| DEVICE_MANUFACTURER |
| LOCAL_SALES_START_DTTM |

