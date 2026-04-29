# VYA_SUBSCR_PERIOD_EXITQV

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies and consolidates potentially overlapping or contiguous subscription records into distinct, non-overlapping subscription periods for a specific source system (ID 42). It assigns a unique row number, a period number within each subscription, the start and end dates of the consolidated period, flags the latest period, and includes the original count of records for that subscription.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SOURCE_SYSTEM_ID |
| START_DATE |
| END_DATE |
| PRODUCT_OFFER_ID |

