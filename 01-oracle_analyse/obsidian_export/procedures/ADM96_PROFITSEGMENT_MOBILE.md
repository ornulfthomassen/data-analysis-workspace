# ADM96_PROFITSEGMENT_MOBILE

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure extracts and consolidates subscription segment data from various source systems, creating an intermediate raw dataset. It then processes this raw data to refine the end dates for subscription segments, ensuring continuity or non-overlapping periods, and stores the final processed data in a permanent 'profit segment' table for mobile subscriptions. It also manages table existence (dropping previous versions), sets parallelism, gathers statistics, and creates necessary indexes for both intermediate and final tables.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
- ← [[CCDW_SEGMENT.SUBSCRIPTION_SEGMENT]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| START_DATE |
| END_DATE |
| SEGMENT_ID |
| MODEL_ID |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SOURCE_SYSTEM_KEY |
| SUBSCRIPTION_ID |
- ← [[CLM_ADM.ADM_PROFIT_CAT_SUBS_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SUBSCR_ID |
| CATEGORY |
| PERIOD_MONTH_KEY |
- ← [[CRM_ANALYSE.ADM_MONTH_DIM]]
| Column Name |
|---|
| FIRST_DATE |
| LAST_DATE |
| PREV2_PERIOD_MONTH_KEY |
| PERIOD_MONTH_KEY |
- ← [[CRM_ANALYSE.PROFITSEGMENT_MOBILE_RAW]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SUBSCR_ID |
| START_DATE |
| END_DATE |
| SEGMENT_ID |
| MODEL_ID |
| RAD |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.PROFITSEGMENT_MOBILE_RAW]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SUBSCR_ID |
| START_DATE |
| END_DATE |
| SEGMENT_ID |
| MODEL_ID |
| RAD |
- → [[CRM_ANALYSE.PROFITSEGMENT_MOBILE]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SUBSCR_ID |
| START_DATE |
| END_DATE |
| REAL_END_DATE |
| SEGMENT_ID |
| MODEL_ID |

