# KIM_PROFIT_SEGMENT_HIST_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies the historical profit segment (category) for each unique combination of subscription key, contact month key, and source system key. It retrieves the latest category from the `PROFIT.CP_CAT_BED_PRIV` table, based on `PERIOD_ID`, that chronologically precedes the `CONTACT_MONTH_KEY` from `KIM_CAMPAIGN_DETAIL_FACT` and is after January 2012. The view also includes a default dummy row with values -1 for all columns, likely for reporting or placeholder purposes.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[PROFIT.CP_CAT_BED_PRIV]]

