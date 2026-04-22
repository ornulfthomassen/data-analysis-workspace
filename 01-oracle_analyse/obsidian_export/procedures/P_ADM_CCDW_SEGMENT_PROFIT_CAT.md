# P_ADM_CCDW_SEGMENT_PROFIT_CAT

**Schema:** `CCM` | **Type:** `Procedure`

## Description
The procedure P_ADM_CCDW_SEGMENT_PROFIT_CAT calculates and inserts segment-specific profit data for subscriptions into the CCDW_SEGMENT.SEGM_SUBSC_DATA table. It uses Common Table Expressions (CTEs) to gather and process data from various sources related to subscription segments, profit categories, models, and current profit periods. The process involves aggregating data, calculating cumulative distribution values, and deriving relevant dates (e.g., `START_DATE`, `END_DATE`) before inserting the final, processed records. A final check ensures the number of records generated matches the intended number for insertion, and it considers prior load status (ANTALL_IKKE_LASTET) for 'Kundelønnsomhet' (Customer Profitability).

## Data Sources (Inputs)
- ← [[CCDW_SEGMENT.SUBSCRIPTION_SEGMENT]]
- ← [[CRM_ANALYSE.ADM_CURRENT_SUBS_PROFIT_PERIOD]]
- ← [[CCDW_SEGMENT.SEGM_SUBSC_DATA]]
- ← [[CLM_ADM.ADM_PROFIT_CAT_SUBS_HIST]]
- ← [[CCDW_SEGMENT.MODEL]]
- ← [[CCDW_SEGMENT.SEGMENT]]

## Target Tables (Outputs)
- → [[CCDW_SEGMENT.SEGM_SUBSC_DATA]]

