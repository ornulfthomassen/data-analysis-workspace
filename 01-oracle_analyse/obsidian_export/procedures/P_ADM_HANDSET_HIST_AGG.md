# P_ADM_HANDSET_HIST_AGG

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Aggregates handset history data from the `CLM_ADM.ADM_SUBSCR_HANDSET_HIST_AGG` table by model identifier (MODELID). It calculates counts of records and determines the first/last period month keys, terminal usage dates, and various first/last attributes related to the device producer, model, OS type, category, touch screen, device type, HD voice, and LTE capabilities. The aggregated results are stored in the `ADM_HANDSET_HIST_AGG` table, which is completely rebuilt (dropped and recreated) for the specified period after validating the availability and status of necessary source data from `GALAXY.DATE_DIM_MV` and `CLM_ADM.ADM_SUBSCR_HANDSET_HIST_AGG` itself.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[CLM_ADM.ADM_SUBSCR_HANDSET_HIST_AGG]]
| Column Name |
|---|
| LAST_PERIOD_MONTH_KEY |
| MODELID |
| FIRST_PERIOD_MONTH_KEY |
| TERMINAL_USE_FIRST_DATE |
| TERMINAL_USE_LAST_DATE |
| FIRST_PRODUCERNAME |
| LAST_PRODUCERNAME |
| FIRST_MODELNAME |
| LAST_MODELNAME |
| FIRST_DEVICE_OS_TYPE |
| LAST_DEVICE_OS_TYPE |
| FIRST_DEVICE_CATEGORY |
| LAST_DEVICE_CATEGORY |
| FIRST_DEVICE_TOUCH_SCREEN |
| LAST_DEVICE_TOUCH_SCREEN |
| FIRST_DEVICE_TYPE |
| LAST_DEVICE_TYPE |
| FIRST_DEVICE_HD_VOICE |
| LAST_DEVICE_HD_VOICE |
| FIRST_DEVICE_LTE |
| LAST_DEVICE_LTE |

## Target Tables (Outputs)
- → [[ADM_HANDSET_HIST_AGG]]
| Column Name |
|---|
| MODEL_KEY |
| ANTALL |
| FIRST_PERIOD_MONTH_KEY |
| LAST_PERIOD_MONTH_KEY |
| TERMINAL_USE_FIRST_DATE |
| TERMINAL_USE_LAST_DATE |
| FIRST_PRODUCERNAME |
| LAST_PRODUCERNAME |
| FIRST_MODELNAME |
| LAST_MODELNAME |
| FIRST_DEVICE_OS_TYPE |
| LAST_DEVICE_OS_TYPE |
| FIRST_DEVICE_CATEGORY |
| LAST_DEVICE_CATEGORY |
| FIRST_DEVICE_TOUCH_SCREEN |
| LAST_DEVICE_TOUCH_SCREEN |
| FIRST_DEVICE_TYPE |
| LAST_DEVICE_TYPE |
| FIRST_DEVICE_HD_VOICE |
| LAST_DEVICE_HD_VOICE |
| FIRST_DEVICE_LTE |
| LAST_DEVICE_LTE |

