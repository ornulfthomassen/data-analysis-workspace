# ADM_HANDSET_HIST_AGG_V

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates handset history data from the 'ADM_SUBSCR_HANDSET_HIST_AGG' table by 'MODEL_KEY'. It calculates the total count ('ANTALL') for each model key and determines the earliest and latest values for various period keys, dates, and device characteristics (like producer name, model name, OS type, category, touch screen, device type, HD voice, and LTE support).

## Data Sources (Inputs)
- ← [[ADM_SUBSCR_HANDSET_HIST_AGG]]
| Column Name |
|---|
| MODEL_KEY |
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

