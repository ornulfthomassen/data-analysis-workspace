# V_ANALYSE_USE_AGG_MAINNUMBER

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates detailed usage and revenue data from a consumption usage table (`CON_USAGE_AGG`) by period, main phone number, user customer, and business area, calculating sums of various call minutes, SMS/MMS counts, data volumes, and revenues, along with the latest event dates for mobile and fixed services.

## Data Sources (Inputs)
- ← [[CCDW_CONSUMERANALYSE.CON_USAGE_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| MAIN_NUMBER |
| USER_CUSTOMER_KEY |
| BUSINESS_AREA_KEY |
| MOB_COMP_CALLS_MIN |
| MOB_FIXED_CALLS_MIN |
| MOB_TNM_CALLS_MIN |
| MOB_ABROAD_CALLS_MIN |
| MOB_INCL_MIN_CALLS_MIN |
| MOB_TOT_MIN |
| MOB_SMS_NUM |
| MOB_MMS_NUM |
| MOB_TERM_CALLS_NUM |
| MOB_TERM_CALLS_MIN |
| MOB_OUT_CALLS_NUM |
| MOB_INCL_MIN_CALLS_NUM |
| MOB_SMALL_SCR_VOL |
| MOB_BIG_SCR_VOL |
| MOB_LAST_EVENT_DATE |
| FIXED_MOB_CALLS_MIN |
| FIXED_REMOTE_CALLS_MIN |
| FIXED_LOCAL_CALLS_MIN |
| FIXED_OTHER_CALLS_MIN |
| FIXED_FOREIGN_CALLS_MIN |
| FIXED_COMP_CALLS_MIN |
| FIXED_MOB_CALLS_NUM |
| FIXED_REMOTE_CALLS_NUM |
| FIXED_LOCAL_CALLS_NUM |
| FIXED_OTHER_CALLS_NUM |
| FIXED_FOREIGN_CALLS_NUM |
| FIXED_COMP_CALLS_NUM |
| FIXED_LAST_EVENT_DATE |
| VOLUME_DOWN |
| VOLUME_TOTAL |
| NET_REVENUE |
| GROSS_REVENUE |

