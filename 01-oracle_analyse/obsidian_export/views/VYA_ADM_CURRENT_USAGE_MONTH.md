# VYA_ADM_CURRENT_USAGE_MONTH

**Schema:** `CCM` | **Type:** `View`

## Description
This view, VYA_ADM_CURRENT_USAGE_MONTH, is designed to retrieve and present data for the 'current' or most recent relevant month, along with information for the three preceding months. It identifies the 'current' month by finding the maximum PERIOD_MONTH_KEY from the CLM_ADM.ADM_SUBS_USAGE_MOB_MONTH_AGG table (excluding keys >= 999912). The view then selects period details like month character, key, date, and number of days (ANTALL_DAGER) for this identified current month and its three previous months. Its purpose, as stated in the comments, is for 'Loading Current_Usage Month to Mjøsa', suggesting it's used for populating a data warehouse or reporting system with up-to-date and historical monthly usage period information.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_SUBS_USAGE_MOB_MONTH_AGG]]

