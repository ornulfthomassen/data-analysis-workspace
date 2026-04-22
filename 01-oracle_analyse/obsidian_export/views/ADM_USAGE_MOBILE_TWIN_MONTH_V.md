# ADM_USAGE_MOBILE_TWIN_MONTH_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and summarizes mobile usage data (MMS, SMS, voice calls, and data) and associated net revenue for subscriptions associated with 'TWIN' and 'DATATWIN' services. The data is grouped by relative month, period month key, subscription ID, and sub-number, covering the current month and the preceding five months. It provides detailed breakdowns of usage and revenue by service type (MMS, SMS, TALE, Data) and geographical categories (domestic, international EU, international ROW, roaming EU, roaming ROW), including various data usage categories like zero-rated, included, invoiced, package-related, and shared buckets. This view is intended for Customer Lifecycle Management (CLM) and Business Intelligence reporting.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
- ← [[CLM_ADM.ADM_SUBS_USAGE_MOB_MONTH_AGG]]

