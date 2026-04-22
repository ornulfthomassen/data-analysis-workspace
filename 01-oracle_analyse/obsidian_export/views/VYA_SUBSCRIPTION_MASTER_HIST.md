# VYA_SUBSCRIPTION_MASTER_HIST

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a standardized and formatted representation of historical subscription master data. It primarily casts various columns from its source table to specific CHAR data types and lengths. The view name and column suffixes (e.g., _PREV, _ORIG, _PAST) indicate that it contains historical tracking information for subscriptions, including details like original start dates, previous states, market areas, product keys, and porting information. It serves to expose this detailed historical subscription data in a consistent format, likely for reporting, analytics, or integration purposes.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]

