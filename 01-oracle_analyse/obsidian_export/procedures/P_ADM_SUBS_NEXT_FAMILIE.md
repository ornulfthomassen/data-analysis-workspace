# P_ADM_SUBS_NEXT_FAMILIE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Processes subscription data for a given month, populating and maintaining partitioned detail and aggregated tables. It first extracts detailed subscription product information into a temporary table, then moves this data into a permanent partitioned detail table. Subsequently, it aggregates this detailed information into another temporary table, which is then moved into a permanent partitioned aggregate table.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SUBSCRIPTION_SEQ |
| PRODUCT_OFFER_ID |
| START_DATE |
| END_DATE |
| BUSINESS_AREA_ID |
- ← [[CLM_ADM.ADM_SUBS_NEXT_FAMILIE_DET]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SUBSCRIPTION_SEQ |
| PRODUCT_OFFER_ID |
| END_DATE |
| PERIOD_MONTH_KEY |

## Target Tables (Outputs)
- → [[CLM_ADM.TMP_SUBS_NEXT_FAMILIE_DET]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| SUBSCRIPTION_SEQ |
| PRODUCT_OFFER_ID |
| START_DATE |
| END_DATE |
- → [[CLM_ADM.ADM_SUBS_NEXT_FAMILIE_DET]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| SUBSCRIPTION_SEQ |
| PRODUCT_OFFER_ID |
| START_DATE |
| END_DATE |
- → [[CLM_ADM.TMP_SUBS_NEXT_FAMILIE_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| LAST_SUBSCRIPTION_SEQ |
| LAST_PRODUCT_OFFER_ID |
| MAX_END_DATE |
| ANTALL |
- → [[CLM_ADM.ADM_SUBS_NEXT_FAMILIE_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| LAST_SUBSCRIPTION_SEQ |
| LAST_PRODUCT_OFFER_ID |
| MAX_END_DATE |
| ANTALL |

