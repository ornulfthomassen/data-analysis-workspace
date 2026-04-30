# ADM_SUBSCR_HANDSET_HIST_AGG_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates historical handset usage data per subscription and model ID. For each unique combination of subscription and model, it identifies the earliest and latest period months, the overall first and last terminal usage dates, and captures specific handset attributes (such as producer name, model name, OS type, category, touch screen, type, HD voice, and LTE capability) corresponding to both the earliest and latest recorded periods. It filters out a specific model ID.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBSCR_HANDSET_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PERIOD_MONTH_KEY |
| TERMINAL_USE_FIRST_DATE |
| TERMINAL_USE_LAST_DATE |
| MODELID |
| PRODUCERNAME |
| MODELNAME |
| DEVICE_OS_TYPE |
| DEVICE_CATEGORY |
| DEVICE_TOUCH_SCREEN |
| DEVICE_TYPE |
| DEVICE_HD_VOICE |
| DEVICE_LTE |


