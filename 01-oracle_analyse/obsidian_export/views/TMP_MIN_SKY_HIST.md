# TMP_MIN_SKY_HIST

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates monthly historical 'Min Sky' (My Sky) usage, subscription, and activity data. It joins dimensional month information with 'Min Sky' historical metrics and global user subscription history, providing a detailed snapshot of various metrics like storage quota, usage, device connections, file operations (upload, download, delete), mobile platform statistics, and first-use details. It also includes filters to exclude specific problematic records (duplicates) and certain months.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY_CHAR |
| LAST_DATE |
| PERIOD_MONTH_KEY |
- ← [[CLM_ADM.ADM_MIN_SKY_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| GLOBAL_ID_CHAR |
| CREATION_DTTM |
| LAST_FILE_EVENT_DTTM |
| LAST_CONNECTION_DTTM |
| LAST_UPLOAD_DTTM |
| LAST_MOB_CONNECTION_DTTM |
| LAST_MOB_UPLOAD_DTTM |
| GB_QUOTA |
| PCT_MB_USED |
| MB_USED |
| NO_DEVICE_CONNECTED |
| NO_DEVICE_UPLOAD |
| NO_DEVICES |
| NO_FILES_UPLOAD |
| NO_FILES_DOWNLOAD |
| NO_FILES_DELETE |
| NO_MOB_DEVICE_CONNECTED |
| NO_MOB_DEVICE_UPLOAD |
| NO_MOB_DEVICES_TOT |
| MOBILE_PLATFORM_ANDROID_TOT |
| MOBILE_PLATFORM_APPLE_TOT |
| SUM_MOB_AUTO_UPLOAD |
| MAX_ANDROID_OS_VERSION |
| MAX_APPLE_OS_VERSION |
| MAX_ANDROID_CLIENT_VERSION |
| MAX_APPLE_CLIENT_VERSION |
| NO_MOB_FILES_UPLOAD |
| NO_MOB_FILES_DOWNLOAD |
| NO_MOB_FILES_DELETE |
| PERIOD_MONTH_KEY |
| GLOBAL_ID |
- ← [[CLM_ADM.ADM_GLOBAL_USER_SUBS_HIST]]
| Column Name |
|---|
| MIN_SKY_NO_DAYS_FIRST_USE |
| FIRST_EVENT_DTTM |
| PERIOD_MONTH_KEY |
| COMOYO_USER_ID |

