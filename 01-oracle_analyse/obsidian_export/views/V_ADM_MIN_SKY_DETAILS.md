# V_ADM_MIN_SKY_DETAILS

**Schema:** `CCM` | **Type:** `View`

## Description
The view `V_ADM_MIN_SKY_DETAILS` combines subscription details with Min Sky service activation events to derive first usage information. It enriches this data with a wide array of historical aggregated usage metrics, such as data quota, MB used, number of devices connected, and file upload/download/delete counts, for several preceding months. The purpose is to provide a comprehensive analytical dataset for understanding Min Sky subscriber characteristics, service adoption, and usage patterns over time, filtered for relevant activation events and recent historical data.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| KURT_ID_OWNER |
| KURT_ID_USER |
| MARKET_AREA_ID |
| BUSINESS_AREA_ID |
| PARENT_SUBSCRIPTION_ID |
- ← [[GALAXY.SUBSCRIPTION_DIM_MV]]
| Column Name |
|---|
| SUBSCRIPTION_KEY |
| COMOYO_USER_ID |
- ← [[COMOYO.COMOYO_SUB_GRANT_EVENTS]]
| Column Name |
|---|
| USER_ID |
| EVENT_TIME |
| LOAD_DATE |
| EVENT |
- ← [[CRM_ANALYSE.ADM_MIN_SKY_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| GLOBAL_ID_CHAR |
| CREATION_DTTM |
| LAST_FILE_EVENT_DTTM |
| LAST_CONNECTION_DTTM |
| LAST_UPLOAD_DTTM |
| LAST_MOB_CONNECTION_DTTM |
| LAST_MOB_UPLOAD_DTTM |
| GB_QUOTA_PREV1 |
| PCT_MB_USED_PREV1 |
| MB_USED_PREV1 |
| MB_USED_PREV2 |
| MB_USED_PREV3 |
| NO_DEVICE_CONNECTED_LAST1 |
| NO_DEVICE_CONNECTED_LAST2 |
| NO_DEVICE_CONNECTED_LAST3 |
| NO_DEVICE_UPLOAD_LAST1 |
| NO_DEVICE_UPLOAD_LAST2 |
| NO_DEVICE_UPLOAD_LAST3 |
| NO_DEVICES |
| NO_FILES_UPLOAD_PREV1 |
| NO_FILES_UPLOAD_PREV2 |
| NO_FILES_UPLOAD_PREV3 |
| NO_FILES_DOWNLOAD_PREV1 |
| NO_FILES_DOWNLOAD_PREV2 |
| NO_FILES_DOWNLOAD_PREV3 |
| NO_FILES_DELETE_PREV1 |
| NO_FILES_DELETE_PREV2 |
| NO_FILES_DELETE_PREV3 |
| NO_MOB_DEVICE_CONNECTED_LAST1 |
| NO_MOB_DEVICE_UPLOAD_LAST1 |
| NO_MOB_DEVICES_TOT |
| NO_MOB_DEVICES_NEW |
| MOBILE_PLATFORM_ANDROID_TOT |
| MOB_PLATFORM_ANDROID_NEW |
| MOBILE_PLATFORM_APPLE_TOT |
| MOB_PLATFORM_APPLE_NEW |
| SUM_MOB_AUTO_UPLOAD |
| MAX_ANDROID_OS_VERSION |
| MAX_APPLE_OS_VERSION |
| MAX_ANDROID_CLIENT_VERSION |
| MAX_APPLE_CLIENT_VERSION |
| NO_MOB_FILES_UPLOAD_PREV1 |
| NO_MOB_FILES_UPLOAD_PREV2 |
| NO_MOB_FILES_UPLOAD_PREV3 |
| NO_MOB_FILES_DOWNLOAD_PREV1 |
| NO_MOB_FILES_DOWNLOAD_PREV2 |
| NO_MOB_FILES_DOWNLOAD_PREV3 |
| NO_MOB_FILES_DELETE_PREV1 |
| NO_MOB_FILES_DELETE_PREV2 |
| NO_MOB_FILES_DELETE_PREV3 |
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| YEAR_MONTH_NUMBER |
| RELATIVE_MONTH |
- ← [[CRM_ANALYSE.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| FIRST_DATE |

