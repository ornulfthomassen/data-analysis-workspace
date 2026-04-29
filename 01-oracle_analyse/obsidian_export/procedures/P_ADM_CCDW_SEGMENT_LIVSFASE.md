# P_ADM_CCDW_SEGMENT_LIVSFASE

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This procedure conditionally inserts customer segment data into the 'CCDW_SEGMENT.SEGM_CUST_DATA' table. It aggregates customer life-phase segment information from a view, enriches it with model and segment metadata, and only proceeds with the insertion if no existing 'Livsfase CLM' data is found in the target table.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.V_CLM_LIVSFASE_SEGMENT]]
| Column Name |
|---|
| KURT_ID |
| PERIOD_MONTH_KEY |
| CLM_LIVSFASE_SEGMENT |
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
- ← [[CCDW_SEGMENT.SEGM_CUST_DATA]]
| Column Name |
|---|
| MODEL_NAME |

## Target Tables (Outputs)
- → [[CCDW_SEGMENT.SEGM_CUST_DATA]]
| Column Name |
|---|
| MODEL_NAME |
| SEGMENT_NAME |
| CUSTOMER_KURT_ID |
| SEGMENT_START_DATE |
| SEGMENT_END_DATE |
| SCORE_MEASSURE |
| SCORE_DATE |
| LOAD_DATE |

