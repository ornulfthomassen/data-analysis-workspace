# P_ADM_CUST_NEXT_FAMILIE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Aggregates customer subscription data to count specific product offers per customer for a given month, storing the results in a partitioned aggregate table. It first creates a temporary table with aggregated data and then uses a partition exchange operation to insert this data into the permanent target table.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| CUSTOMER_SK_OWNER |
- ← [[ADM_SUBS_NEXT_FAMILIE_AGG]]
| Column Name |
|---|
| LAST_PRODUCT_OFFER_ID |
| SUBSCRIPTION_ID |
| PERIOD_MONTH_KEY |
| MAX_END_DATE |
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| LAST_DATE |

## Target Tables (Outputs)
- → [[CLM_ADM.TMP_CUST_NEXT_FAMILIE_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK_OWNER |
| ANT_RAB_NEXT_FAM_VOKSEN |
| ANT_RAB_NEXT_FAM_U18 |
- → [[ADM_CUST_NEXT_FAMILIE_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK_OWNER |
| ANT_RAB_NEXT_FAM_VOKSEN |
| ANT_RAB_NEXT_FAM_U18 |

