# P_ADM_SUBSCR_DET_HIST_FB

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Calculates and loads monthly family bonus activity details for subscriptions into a partitioned history table, `ADM_SUBSCR_DET_HIST_FB`, for a specified month. It checks for the availability of source data, creates a temporary table with the calculated details, and then exchanges this temporary table with the target partition, effectively replacing or inserting the monthly data.

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
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
| Column Name |
|---|
| START_DATE |
| BUSINESS_AREA_ID |
| PRODUCT_OFFER_ID |
| SUBSCRIPTION_ID |
| END_DATE |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| SOURCE_SYSTEM_NAME |
| SOURCE_PRODUCT_ID_1 |
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| LAST_DATE |
| PERIOD_MONTH_KEY |

## Target Tables (Outputs)
- → [[TMP_SUBSCR_DET_HIST_FB]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| FAMILY_BONUS_ACTIVE |
| FB_NO_DAYS_ACTIVE |
| NO_FAMILY_BONUS |
| FB_NO_DAYS_FIRST_START |
| FB_NO_DAYS_LAST_START |
| FB_NO_DAYS_FIRST_END |
| FB_NO_DAYS_LAST_END |
- → [[ADM_SUBSCR_DET_HIST_FB]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| FAMILY_BONUS_ACTIVE |
| FB_NO_DAYS_ACTIVE |
| NO_FAMILY_BONUS |
| FB_NO_DAYS_FIRST_START |
| FB_NO_DAYS_LAST_START |
| FB_NO_DAYS_FIRST_END |
| FB_NO_DAYS_LAST_END |

