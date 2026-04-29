# ADM23_HOUSEHOLD_SUBS_CNT

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure calculates and aggregates household subscription counts and activity metrics by month. It manages a partitioned target table, `CRM_ANALYSE.ADM_HOUSEHOLD_SUBS_CNT`, creating it if necessary (including partitions and unique indexes). It then populates this table with derived statistics from various CRM and CLM data sources for a specified range of months, performs data availability checks, and logs processing status using an external procedure.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
| SUBOBJECT_NAME |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[CRM_ANALYSE.ADM_HOUSEHOLD_INFO_KURT_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| HOUSEHOLD_ID |
| KURT_ID |
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| KURT_ID_USER |
| BUSINESS_AREA_ID |
| PRODUCT_BRAND |
| SUBS_NO_DAYS_ACTIVE |
| SUBSCRIPTION_ID |
- ← [[CLM_ADM.ADM_SUBSCR_DETAIL_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| SUBS_TYPE |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| MB_TOT_PREV1 |
| NUMBER_OF_MMS_NORGE_PREV1 |
| NUMBER_OF_SMS_NORGE_PREV1 |
| NUMBER_OF_SMS_UTLAND_PREV1 |
| NUMBER_SPEECH_NORGE_PREV1 |
| NUMBER_SPEECH_UTLAND_PREV1 |
- ← [[DUAL]]
- ← [[CRM_ANALYSE.ADM_HOUSEHOLD_SUBS_CNT]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_HOUSEHOLD_SUBS_CNT]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| HOUSEHOLD_ID |
| HH_NO_KURT_ID_USER |
| HH_NO_MPP_USR |
| HH_NO_MPR_USR |
| HH_NO_MPR_USR_ACTIVE |
| HH_NO_MBB_USR |
| HH_NO_FIX_USR |
| HH_NO_DSL_USR |
| HH_NO_FBR_USR |
| HH_NO_TNM_SUBSR_USR |
| HH_NO_DJU_SUBSR_USR |
| HH_MPP_NO_DAYS_ACTIVE |
| HH_MPR_NO_DAYS_ACTIVE |
| HH_MBB_NO_DAYS_ACTIVE |
| HH_FIX_NO_DAYS_ACTIVE |
| HH_DSL_NO_DAYS_ACTIVE |
| HH_FIB_NO_DAYS_ACTIVE |
| HH_NO_MPP_BUS_SUBS_USR |
| HH_NO_MBB_BUS_SUBS_USR |
| HH_NO_FIX_BUS_SUBS_USR |
| HH_NO_DSL_BUS_SUBS_USR |
| HH_NO_FBR_BUS_SUBS_USR |
| HH_MPP_BUS_NO_DAYS_ACTIVE |
| HH_MBB_BUS_NO_DAYS_ACTIVE |
| HH_FIX_BUS_NO_DAYS_ACTIVE |
| HH_DSL_BUS_NO_DAYS_ACTIVE |
| HH_FBR_BUS_NO_DAYS_ACTIVE |

