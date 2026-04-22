# GCP_SUBS_USAGE_MONTH_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a monthly aggregated snapshot of mobile subscription usage and associated revenue metrics. It details usage amounts (MMS, SMS, Voice/TALE, Data in MB) and net revenues, categorized by domestic, international (EU/ROW), roaming (EU/ROW), and various data package/bucket types. The view specifically filters to display data only for the latest *complete* month available in the source system, typically the previous month's finalized data.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBS_USAGE_MOB_MONTH_AGG]]

