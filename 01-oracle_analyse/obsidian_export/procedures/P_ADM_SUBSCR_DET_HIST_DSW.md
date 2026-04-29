# P_ADM_SUBSCR_DET_HIST_DSW

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure calculates and stores historical subscription details related to 'Data Switch' products for a given month (P_YYYYMM). It performs data validation against several source tables, creates a temporary table to aggregate and process the data, and then exchanges a partition in the permanent target table (ADM_SUBSCR_DET_HIST_DSW) with the processed data. The procedure handles partitioning, error logging via an external procedure `CRM_ANALYSE.P_ADM_LOAD_HISTORY`, and ensures data integrity by checking for existing data before overwriting.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| PRODUCT_OFFER_ID |
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
| Column Name |
|---|
| START_DATE |
| SUBSCRIPTION_ID |
| END_DATE |
| PRODUCT_OFFER_ID |
| BUSINESS_AREA_ID |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_NAME |
| PRODUCT_KEY |
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| LAST_DATE |
| PERIOD_MONTH_KEY |
- ← [[ADM_SUBSCR_DET_HIST_DSW]]

## Target Tables (Outputs)
- → [[ADM_SUBSCR_DET_HIST_DSW]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| DSWITCH_NO_DAYS_FIRST_START |
| DSWITCH_NO_DAYS_LAST_START |
| DSWITCH_NO_DAYS_FIRST_END |
| DSWITCH_NO_DAYS_LAST_END |
| DSWITCH_NO_DAYS_ACTIVE |
| NO_DSWITCH |
- → [[TMP_SUBSCR_DET_HIST_DSW]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| DSWITCH_NO_DAYS_FIRST_START |
| DSWITCH_NO_DAYS_LAST_START |
| DSWITCH_NO_DAYS_FIRST_END |
| DSWITCH_NO_DAYS_LAST_END |
| DSWITCH_NO_DAYS_ACTIVE |
| NO_DSWITCH |

