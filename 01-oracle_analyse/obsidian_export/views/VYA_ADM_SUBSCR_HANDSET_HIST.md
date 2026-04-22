# VYA_ADM_SUBSCR_HANDSET_HIST

**Schema:** `CCM` | **Type:** `View`

## Description
This view combines monthly period information with historical subscription and handset (device) usage data, linking subscriptions to main IDs and enriching device details with range information. It also calculates monthly and next-monthly composite keys for subscriptions and main IDs. Its primary use is for loading subscription data into a target system named 'Mjøsa'.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_SUBSCR_HANDSET_HIST]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[CLM_ADM.ADM_DEVICE_RANGE_DIM]]

