# ADM_PAST_ORIG_SUBS_MASTER2

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL function, `ADM_PAST_ORIG_SUBS_MASTER2`, aims to identify the ultimate original or 'root' subscription ID within a potentially hierarchical or linked structure of subscription records. It does this by taking a `SUBSCRIPTION_ID` as input, querying a master subscription table to find related 'past' or 'previous' subscription IDs, and then recursively calling itself with the newly found ID until a 'root' condition ('OK%') is met, or no data is found.

## Data Sources (Inputs)
- ← [[ADM_MOB_SUBSCR_MASTER_RAW2]]

