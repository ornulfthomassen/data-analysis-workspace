# ADM99_VARSEGMENT_MOBILE

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Transforms raw subscription segment data into a finalized mobile segmentation table. It first extracts and ranks segments into an intermediate table, then processes this intermediate data to refine segment end dates, aiming to 'fill gaps' between consecutive segments for the same subscription, and stores the result in a permanent segmentation table.

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
- ← [[CRM_ANALYSE.VARSEGMENT_MOBILE_RAW]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| START_DATE |
| END_DATE |
| SEGMENT_ID |
| PAY_TYPE |
| MODEL_ID |
| RAD |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.VARSEGMENT_MOBILE_RAW]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| START_DATE |
| END_DATE |
| SEGMENT_ID |
| PAY_TYPE |
| MODEL_ID |
| RAD |
- → [[CRM_ANALYSE.VARSEGMENT_MOBILE]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| START_DATE |
| END_DATE |
| REAL_END_DATE |
| SEGMENT_ID |
| PAY_TYPE |
| MODEL_ID |

