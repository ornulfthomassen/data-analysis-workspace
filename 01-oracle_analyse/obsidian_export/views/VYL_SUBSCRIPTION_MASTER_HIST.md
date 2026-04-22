# VYL_SUBSCRIPTION_MASTER_HIST

**Schema:** `CCM` | **Type:** `View`

## Description
This view, VYL_SUBSCRIPTION_MASTER_HIST, provides a standardized and comprehensive historical record of subscription master data. It includes current and various historical states (original, previous, past, past original) for numerous subscription attributes such as IDs, market areas, start/end dates, product keys, and porting information. The view specifically filters for subscriptions that are currently active (END_DATE IS NULL) or have ended relatively recently (from the beginning of the previous month). The extensive use of CAST operations indicates data type standardization for output.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]

