# GCP_ADM_CUSTOMER_USER_SUBS_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive aggregated monthly summary of customer subscription details. It includes various metrics such as gross and net fees, usage (data, MMS, SMS, voice), and counts of subscriptions broken down by different service types (e.g., Mobile Postpaid (MPP), Mobile Prepaid (MPR), Mobile Broadband (MBB), Fixed Line (FIX), DSL, Fiber (FBR)). The view also tracks the number of active days and product changes for each service type, as well as historical usage metrics (for the last 1, 2, and 3 periods) for data, MMS, SMS, and voice (domestic and international). It distinguishes between general and business subscriptions for certain service types.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_USER_SUBS_AGG]]

