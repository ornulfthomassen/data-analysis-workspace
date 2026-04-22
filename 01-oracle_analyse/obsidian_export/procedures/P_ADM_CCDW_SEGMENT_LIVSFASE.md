# P_ADM_CCDW_SEGMENT_LIVSFASE

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `P_ADM_CCDW_SEGMENT_LIVSFASE`, calculates and populates customer life-phase segmentation data into the `CCDW_SEGMENT.SEGM_CUST_DATA` table. It aggregates customer life-phase segments from `CRM_ANALYSE.V_CLM_LIVSFASE_SEGMENT` and joins this with model and segment definitions from `CCDW_SEGMENT.MODEL` and `CCDW_SEGMENT.SEGMENT` for a specific `MODEL_ID` (40). A crucial check is performed: the data insertion into `CCDW_SEGMENT.SEGM_CUST_DATA` only proceeds if there are no existing records with `MODEL_NAME = 'Livsfase CLM'` in that table, acting as a guard condition to prevent duplicate or uncontrolled loading. The procedure assigns a segment start date of `SYSDATE` and an end date of `SYSDATE + 730` (approximately two years later) for the new segmentation entries.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.V_CLM_LIVSFASE_SEGMENT]]
- ← [[CCDW_SEGMENT.MODEL]]
- ← [[CCDW_SEGMENT.SEGMENT]]
- ← [[CCDW_SEGMENT.SEGM_CUST_DATA]]

## Target Tables (Outputs)
- → [[CCDW_SEGMENT.SEGM_CUST_DATA]]

