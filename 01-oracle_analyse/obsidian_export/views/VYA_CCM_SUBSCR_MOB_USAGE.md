# VYA_CCM_SUBSCR_MOB_USAGE

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a comprehensive view of mobile subscription usage and revenue metrics, including historical data (last 30 days, last 3 months), averages, and categorized usage groups, to determine subscription activity status. It aggregates and calculates various mobile data, call minute, and revenue figures from different time periods for each subscription.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_SUBSCR_MOB_USAGE_MONTH_V]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MB_HOME_NORMAL_LAST1 |
| MB_HOME_NORMAL_LAST2 |
| MB_HOME_NORMAL_LAST3 |
| MIN_TALE_DOM_LAST1 |
| MIN_TALE_DOM_LAST2 |
| MIN_TALE_DOM_LAST3 |
| NET_REVENUE_LAST1 |
| NET_REVENUE_LAST2 |
| NET_REVENUE_LAST3 |
| MB_DATA_TOT_INCL_FBB_G_LAST1 |
| MB_DATA_TOT_INCL_FBB_G_LAST2 |
| MB_DATA_TOT_INCL_FBB_G_LAST3 |
- ← [[CLM_CCM.CCM_SUBSCR_MOB_USE_V]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PCT_USED_INCL_MB_PROD_AVG_1MO |
| PCT_USED_INCL_MB_PROD_AVG_3MO |
| PCT_P_USE_LAST1_BY_CUR_F_UNIT |
- ← [[CLM_CCM.CCM_SUBSCR_MOB_USAGE_30D_V]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MB_HOME_NORMAL_D30 |
| NET_REVENUE_D30 |
| MB_DATA_TOT_INCL_FBB_G_D30 |
- ← [[CRM_ANALYSE.ADM_MB_GROUP_DIM]]
| Column Name |
|---|
| MB_GROUP_DESC |
| MB_FROM |
| MB_TO |

