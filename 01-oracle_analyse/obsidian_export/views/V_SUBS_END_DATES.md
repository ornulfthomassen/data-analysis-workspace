# V_SUBS_END_DATES

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies the latest subscription end date and the product associated with that latest end date for each unique subscription. It groups the subscription records by `SUBSCRIPTION_ID` and then uses an analytic function (`KEEP (DENSE_RANK LAST ORDER BY S.END_DATE)`) to select the `END_DATE` and `PRODUCT_OFFER_ID` from the record with the most recent `END_DATE` within each subscription group.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]

