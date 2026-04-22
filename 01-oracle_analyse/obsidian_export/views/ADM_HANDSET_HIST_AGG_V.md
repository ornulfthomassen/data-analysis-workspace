# ADM_HANDSET_HIST_AGG_V

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates historical handset data at the MODEL_KEY level. For each unique handset model, it counts the total occurrences ('ANTALL') and determines the earliest and latest values for various period keys (e.g., FIRST_PERIOD_MONTH_KEY, TERMINAL_USE_FIRST_DATE) and device characteristics (e.g., PRODUCERNAME, MODELNAME, DEVICE_OS_TYPE, DEVICE_CATEGORY, DEVICE_TOUCH_SCREEN, DEVICE_TYPE, DEVICE_HD_VOICE, DEVICE_LTE).

## Data Sources (Inputs)
- ← [[ADM_SUBSCR_HANDSET_HIST_AGG]]

