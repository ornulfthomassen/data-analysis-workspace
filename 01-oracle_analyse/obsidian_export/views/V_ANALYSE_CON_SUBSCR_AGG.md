# V_ANALYSE_CON_SUBSCR_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a de-duplicated and aggregated summary of consumer subscription data, selecting the most relevant record for each 'MAIN_NUMBER' based on a complex ranking logic. It aims to resolve potential data inconsistencies and duplicates, particularly for specific historical periods, to present a clean analytical dataset of customer subscriptions, products, and associated attributes like service types (fixed, mobile, internet) and market details.

## Data Sources (Inputs)
- ← [[CCDW_CONSUMERANALYSE.CON_SUBSCR_AGG]]

