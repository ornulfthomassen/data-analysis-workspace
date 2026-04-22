# KIM_MAX_ORDER_DATE_V

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates a cutoff date that is 14 days prior to the latest order date (`ORDER_DT_KEY`) found in the `KIM_CAMPAIGN_DETAIL_FACT` table. This date is returned as a number in YYYYMMDD format.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]

