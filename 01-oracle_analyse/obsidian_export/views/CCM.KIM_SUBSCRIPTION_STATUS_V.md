# KIM_SUBSCRIPTION_STATUS_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies and extracts the latest end date and product offer ID for primary subscriptions. It filters subscriptions by excluding specific source systems (2, 6, 12), including business areas 1 and 2, and ensuring valid main and subscription numbers. The view groups by subscription ID to determine the latest status.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| END_DATE |
| PRODUCT_OFFER_ID |
| PARENT_SUBSCRIPTION_ID |
| SOURCE_SYSTEM_ID |
| BUSINESS_AREA_ID |
| MAIN_NUMBER |


