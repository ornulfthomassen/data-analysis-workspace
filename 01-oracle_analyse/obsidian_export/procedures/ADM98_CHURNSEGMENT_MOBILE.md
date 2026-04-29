# ADM98_CHURNSEGMENT_MOBILE

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure processes raw subscription segment data from `CCDW_SEGMENT.SUBSCRIPTION_SEGMENT` to generate a cleaned and gap-adjusted churn segment table, `CRM_ANALYSE.CHURNSEGMENT_MOBILE`. It first creates an intermediate raw table (`CRM_ANALYSE.CHURNSEGMENT_MOBILE_RAW`) by selecting relevant subscription segments, assigning a payment type, and ranking segments. Then, it uses this raw table to construct the final churn segment table by refining segment end dates to ensure continuity, effectively closing potential gaps between consecutive segments for the same subscription.

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
- ← [[CRM_ANALYSE.CHURNSEGMENT_MOBILE_RAW]]
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
- → [[CRM_ANALYSE.CHURNSEGMENT_MOBILE_RAW]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| START_DATE |
| END_DATE |
| SEGMENT_ID |
| PAY_TYPE |
| MODEL_ID |
| RAD |
- → [[CRM_ANALYSE.CHURNSEGMENT_MOBILE]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| START_DATE |
| END_DATE |
| REAL_END_DATE |
| SEGMENT_ID |
| PAY_TYPE |
| MODEL_ID |

