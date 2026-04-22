# VYA_CCM_SUBSCR_MOB_USAGE

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and presents a comprehensive summary of mobile subscription usage. It includes metrics such as data (MB) consumption, domestic call minutes, and net revenue. These metrics are provided for the last 30 days, the last three individual months, and also as 3-month averages. Additionally, it categorizes MB usage into predefined groups (e.g., 'MB_GROUP_DESC') and determines an overall 'SUBSCRIPTION_USE' status ('Active' or 'Inactive') based on recent activity and revenue across multiple periods.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_SUBSCR_MOB_USAGE_MONTH_V]]
- ← [[CLM_CCM.CCM_SUBSCR_MOB_USE_V]]
- ← [[CLM_CCM.CCM_SUBSCR_MOB_USAGE_30D_V]]
- ← [[CRM_ANALYSE.ADM_MB_GROUP_DIM]]

