# GCP_SUBSCR_MOB_USAGE_MONTH_CURR

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates aggregated current month mobile usage metrics for mobile subscriptions. It retrieves subscription details and joins them with pre-aggregated monthly mobile usage data to provide a comprehensive view of revenue, call minutes, and various data usage categories (e.g., included, invoiced, package, shared bucket, reduced speed) for the current period identified by a specific month key.

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

