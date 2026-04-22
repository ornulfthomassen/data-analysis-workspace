# VYA_FTV_CVIEW_SAVE

**Schema:** `CCM` | **Type:** `View`

## Description
This view is designed to provide a comprehensive dataset for analyzing 'churn save' cases. It extracts detailed information about customer churn attempts, including reasons for saving or termination, associated products, channels, and customer and geographical details. The view specifically filters for cases related to product saves (where SAVE_Product__c is not null), are not deleted, and were created within the last two years.

## Data Sources (Inputs)
- ← [[CVIEW_STAGING.CASE]]
- ← [[CVIEW_STAGING.ACCOUNT]]
- ← [[CVIEW_STAGING.ADDRESS__C]]

