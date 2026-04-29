# ADM97_MAPSEGMENT_MOBILE

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure processes mobile segmentation data by first extracting and transforming historical segment information from `SE_MAP_TOTAL` into an intermediate raw table (`MAPSEGMENT_MOBILE_RAW`), assigning initial start and end dates along with a rank. It then refines these segments by creating a final `ADM_MAPSEGMENT_MOBILE` table, adjusting segment end dates based on the start date of the next consecutive segment for each `KURT_ID`, effectively creating a non-overlapping historical view of segments.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.SE_MAP_TOTAL]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| KURT_ID |
| P_MAP_SEG1 |
| P_MAP_SEG2 |
| P_MAP_SEG3 |
| P_MAP_SEG4 |
| P_MAP_SEG5 |
| P_MAP_SEG6 |
| EM_PROBABILITY |
| BUS_RULE_ALLOCATION |
| FINAL_MAP_SEG |
| START_DATE |
| END_DATE |
- ← [[CRM_ANALYSE.MAPSEGMENT_MOBILE_RAW]]
| Column Name |
|---|
| KURT_ID |
| PERIOD_MONTH_KEY |
| P_MAP_SEG1 |
| P_MAP_SEG2 |
| P_MAP_SEG3 |
| P_MAP_SEG4 |
| P_MAP_SEG5 |
| P_MAP_SEG6 |
| EM_PROBABILITY |
| BUS_RULE_ALLOCATION |
| SEGMENT_ID |
| START_DATE |
| END_DATE |
| RAD |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.MAPSEGMENT_MOBILE_RAW]]
| Column Name |
|---|
| KURT_ID |
| PERIOD_MONTH_KEY |
| P_MAP_SEG1 |
| P_MAP_SEG2 |
| P_MAP_SEG3 |
| P_MAP_SEG4 |
| P_MAP_SEG5 |
| P_MAP_SEG6 |
| EM_PROBABILITY |
| BUS_RULE_ALLOCATION |
| SEGMENT_ID |
| START_DATE |
| END_DATE |
| RAD |
- → [[CRM_ANALYSE.ADM_MAPSEGMENT_MOBILE]]
| Column Name |
|---|
| KURT_ID |
| PERIOD_MONTH_KEY |
| P_MAP_SEG1 |
| P_MAP_SEG2 |
| P_MAP_SEG3 |
| P_MAP_SEG4 |
| P_MAP_SEG5 |
| P_MAP_SEG6 |
| EM_PROBABILITY |
| BUS_RULE_ALLOCATION |
| SEGMENT_ID |
| START_DATE |
| END_DATE |
| REAL_END_DATE |

