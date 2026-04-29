# P_ADM_CCDW_SEGMENT_PROFIT_CAT

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Calculates and inserts subscription profit category data into the `CCDW_SEGMENT.SEGM_SUBSC_DATA` table. The procedure includes a check to ensure that data for the specific 'Kundelønnsomhet' model (identified by MODEL_ID = 19) is only inserted if no such data currently exists in the target table. The inserted data includes model and segment details, subscription identifiers, derived start/end dates, and a profit category measure derived from historical data.

## Data Sources (Inputs)
- ← [[CCDW_SEGMENT.SUBSCRIPTION_SEGMENT]]
| Column Name |
|---|
| START_DATE |
| SEQ_ID |
| SEGMENT_ID |
| MODEL_ID |
- ← [[CRM_ANALYSE.ADM_CURRENT_SUBS_PROFIT_PERIOD]]
| Column Name |
|---|
| PERIOD_ID |
- ← [[CCDW_SEGMENT.SEGM_SUBSC_DATA]]
| Column Name |
|---|
| MODEL |
- ← [[CLM_ADM.ADM_PROFIT_CAT_SUBS_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| SUBSCR_ID |
| MARKET_AREA_ID |
| PAYMENT_TYPE |
| PRODUCT_BRAND |
| SUBS_PERIOD_START_DATE |
| SUBS_DAYS_ACTIVE_IN_PERIOD |
| NET_REVENUE_ADJUSTED |
| CUME_DIST_VALUE |
| CATEGORY |
| PT_CUME_DIST_VALUE |
| PT_CATEGORY |
- ← [[CCDW_SEGMENT.MODEL]]
| Column Name |
|---|
| MODEL_ID |
| MODEL_NAME |
| BUSINESS_AREA_ID |
- ← [[CCDW_SEGMENT.SEGMENT]]
| Column Name |
|---|
| MODEL_ID |
| SEGMENT_ID |
| SEGMENT_NAME |

## Target Tables (Outputs)
- → [[CCDW_SEGMENT.SEGM_SUBSC_DATA]]
| Column Name |
|---|
| MODEL_NAME |
| SEGMENT_NAME |
| BUSINESS_AREA |
| SUBSCRIPTION_ID |
| ACCOUNT_TYPE |
| START_DATE |
| END_DATE |
| MEASURE |
| SCORE_DATE |
| LOAD_DATE |

