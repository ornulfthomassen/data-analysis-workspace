# KIM_MAX_ORDER_DATE_V

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates a date that is 14 days prior to the maximum order date found in the 'KIM_CAMPAIGN_DETAIL_FACT' table, returning it as a number in YYYYMMDD format, specifically considering order dates after 19000101.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| ORDER_DT_KEY |


