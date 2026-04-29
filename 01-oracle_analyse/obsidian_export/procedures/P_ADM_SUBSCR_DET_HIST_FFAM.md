# P_ADM_SUBSCR_DET_HIST_FFAM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Calculates and stores historical 'FriFamilie' product subscription details for a specified month. The procedure first performs data integrity checks on various source tables. If data sources are valid, it creates or ensures the existence of a partition in the target history table. It then populates a temporary table with aggregated subscription data, including the number of active days for 'FriFamilie' products for each subscription, and finally exchanges this temporary table with the corresponding partition in the permanent 'ADM_SUBSCR_DET_HIST_FFAM' table.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_NAME |
| PRODUCT_KEY |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| PRODUCT_OFFER_ID |
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
| Column Name |
|---|
| START_DATE |
| PRODUCT_OFFER_ID |
| SUBSCRIPTION_ID |
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| LAST_DATE |
| PERIOD_MONTH_KEY |
- ← [[ADM_SUBSCR_DET_HIST_FFAM]]

## Target Tables (Outputs)
- → [[TMP_SUBSCR_DET_HIST_FFAM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| FRIFAM_NO_DAYS_ACTIVE |
- → [[ADM_SUBSCR_DET_HIST_FFAM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| FRIFAM_NO_DAYS_ACTIVE |

