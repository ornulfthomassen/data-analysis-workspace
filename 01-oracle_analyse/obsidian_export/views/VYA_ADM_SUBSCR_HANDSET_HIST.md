# VYA_ADM_SUBSCR_HANDSET_HIST

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `VYA_ADM_SUBSCR_HANDSET_HIST`, is designed to consolidate and transform historical subscription handset data. It combines monthly period information, detailed subscription and handset historical records, and device range attributes. Its main purpose is to prepare and stage this combined dataset, including generating new month-specific keys for subscriptions and main IDs, for loading into a data warehouse or analytical system (referred to as 'MJØSA'). The view also renames several source columns to provide a more consistent and descriptive naming convention for the output.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| PERIOD_MONTH_CHAR |
| PERIOD_MONTH_DATE |
| NEXT_PERIOD_MONTH_CHAR |
- ← [[CLM_ADM.ADM_SUBSCR_HANDSET_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| TAC |
| TERMINAL_USE_FIRST_DATE |
| TERMINAL_USE_LAST_DATE |
| MODELID |
| PRODUCERNAME |
| MODELNAME |
| DEVICE_OS_TYPE |
| DEVICE_CATEGORY |
| DEVICE_TYPE |
| DEVICE_HD_VOICE |
| DEVICE_TOUCH_SCREEN |
| DEVICE_LTE |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER_SK |
- ← [[CLM_ADM.ADM_DEVICE_RANGE_DIM]]
| Column Name |
|---|
| DEVICE_KEY |
| DEVICE_RANGE |

