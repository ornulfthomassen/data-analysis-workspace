# TEST_CCM_SUBS_DATA

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates various mobile subscription usage metrics (such as small screen volume, SMS count, data download/total volume, voice call minutes, completed voice call minutes, and gross revenue) for the current month and the two preceding months. This aggregated data is presented per unique main number, user customer key, and subscription owner, enabling analysis of customer usage and revenue trends over a three-month period, likely for CRM or customer communication management purposes.

## Data Sources (Inputs)
- ← [[CCDW_CONSUMERANALYSE.CON_USAGE_AGG]]
- ← [[CCDW.SUBSCRIPTION]]

