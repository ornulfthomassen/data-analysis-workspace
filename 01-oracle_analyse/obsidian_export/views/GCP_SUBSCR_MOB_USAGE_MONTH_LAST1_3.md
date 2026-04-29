# GCP_SUBSCR_MOB_USAGE_MONTH_LAST1_3

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates mobile subscription usage metrics for the last three relative months (current and two preceding months), providing detailed summaries of net revenue, talk minutes, and various data usage categories (e.g., domestic, roaming, package, shared bucket, reduced speed) per subscription, filtering for mobile business area.

## Data Sources (Inputs)
- ← [[CLM_CCM.ODS_SUBSCRIPTION_MV]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| BUSINESS_AREA_ID |
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| RELATIVE_MONTH |
| PERIOD_MONTH_KEY |
- ← [[CLM_ADM.ADM_SUBS_USAGE_MOB_MONTH_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| NET_REVENUE |
| MIN_TALE_DOM |
| MB_DATA |
| MB_DATA_DOM |
| MB_DATA_DOM_INCLUDED |
| MB_DATA_DOM_INVOICED |
| MB_DATA_DOM_REDUCED_SPEED |
| MB_DATA_DOM_PACKAGE_CAMP |
| MB_DATA_DOM_PACKAGE_PAID |
| MB_DATA_DOM_SHARED_BUCKET |
| MB_DATA_ROAM_EU_INCLUDED |
| MB_DATA_ROAM_EU_INVOICED |
| MB_DATA_ROAM_EU_REDUCED_SPEED |
| MB_DATA_ROAM_EU_PACKAGE_CAMP |
| MB_DATA_ROAM_EU_PACKAGE_PAID |
| MB_DATA_ROAM_EU_SHARED_BUCKET |
| MB_DATA_PACKAGE |
| MB_DATA_PACKAGE_FBB_GARANTI |

