# GCP_SUBSCR_MOB_USAGE_MONTH_D30

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates mobile usage and revenue data for subscriptions, specifically for 'PERIOD_MONTH_KEY = 30', by joining detailed monthly usage statistics with subscription master data, and categorizing various types of data usage (normal, package, shared bucket, reduced speed) for domestic and EU roaming.

## Data Sources (Inputs)
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
- ← [[CLM_CCM.ODS_SUBSCRIPTION_MV]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| BUSINESS_AREA_ID |

