# ADM95_LIVSFASESEGMENT_MOBILE

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure processes customer segment data. It first extracts and ranks customer segment records from `CCDW_SEGMENT.CUSTOMER_SEGMENT` into a raw staging table (`CRM_ANALYSE.LIVSFASESEGMENT_MOBILE_RAW`), applying filters for `MODEL_ID` and `END_DATE`. Subsequently, it refines the `END_DATE` values in this raw data, adjusting them based on consecutive segments for the same customer to avoid overlaps or close gaps, and stores the resulting refined segment data in the final `CRM_ANALYSE.LIVSFASESEGMENT_MOBILE` table. The procedure also manages the lifecycle of these tables by dropping them if they exist, gathers statistics, and creates necessary indexes.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
- ← [[CCDW_SEGMENT.CUSTOMER_SEGMENT]]
| Column Name |
|---|
| KURT_ID |
| START_DATE |
| END_DATE |
| SEGMENT_ID |
| MODEL_ID |
- ← [[CRM_ANALYSE.LIVSFASESEGMENT_MOBILE_RAW]]
| Column Name |
|---|
| KURT_ID |
| START_DATE |
| END_DATE |
| SEGMENT_ID |
| MODEL_ID |
| RAD |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.LIVSFASESEGMENT_MOBILE_RAW]]
| Column Name |
|---|
| KURT_ID |
| START_DATE |
| END_DATE |
| SEGMENT_ID |
| MODEL_ID |
| RAD |
- → [[CRM_ANALYSE.LIVSFASESEGMENT_MOBILE]]
| Column Name |
|---|
| KURT_ID |
| START_DATE |
| END_DATE |
| REAL_END_DATE |
| SEGMENT_ID |
| MODEL_ID |

