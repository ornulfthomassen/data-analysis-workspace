# TMP_MIN_SKY_HIST

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `TMP_MIN_SKY_HIST`, consolidates historical monthly data related to 'Min Sky' (My Sky) service usage and global user subscriptions. It combines monthly dimension data with detailed historical records of user activity, device connections, file operations (upload, download, delete), storage quota/usage, and mobile platform information. The purpose is to provide a comprehensive historical overview of 'Min Sky' service engagement and subscription details, excluding specific duplicate records and data for February 2020.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
- ← [[CLM_ADM.ADM_MIN_SKY_HIST]]
- ← [[CLM_ADM.ADM_GLOBAL_USER_SUBS_HIST]]

