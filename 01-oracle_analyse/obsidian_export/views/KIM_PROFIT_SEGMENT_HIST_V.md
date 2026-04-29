# KIM_PROFIT_SEGMENT_HIST_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view combines campaign detail facts with subscription mapping and profit category data. It calculates a 'segment ID' by selecting the latest category based on period ID for each subscription, contact month, and source system key. It includes filtering for active subscriptions and specific period ranges. Additionally, it appends a default record with -1 for all fields, potentially as a placeholder or default return value.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| SUBSCRIPTION_KEY |
| CONTACT_MONTH_KEY |
| SOURCE_SYSTEM_KEY |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SOURCE_SYSTEM_ID |
| SOURCE_SYSTEM_KEY |
- ← [[PROFIT.CP_CAT_BED_PRIV]]
| Column Name |
|---|
| CATEGORY |
| PERIOD_ID |
| SUBSCR_ID |
- ← [[dual]]

