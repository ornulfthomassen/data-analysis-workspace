# P_ADM_MAPSEGMENT_MOBILE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Manages and populates monthly partitions of the `ADM_MAPSEGMENT_MOBILE` table in the `CLM_ADM` schema. It ensures the existence of a specific monthly partition, creates a temporary table by joining customer mapping and segment data for that month, and then atomically exchanges this temporary table with the corresponding partition in the permanent `ADM_MAPSEGMENT_MOBILE` table. This process allows for efficient and atomic updates of historical segment data.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
| SUBOBJECT_NAME |
- ← [[CLM_ADM.ADM_MAPSEGMENT_MOBILE]]
- ← [[CRM_ANALYSE.ADM_MAPSEGMENT_MOBILE]]
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
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_HIST]]
| Column Name |
|---|
| KURT_ID |
| PERIOD_MONTH_KEY |
| CUSTOMER_SK |
- ← [[CLM_ADM.TMP_MAPSEGMENT_MOBILE]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK |
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

## Target Tables (Outputs)
- → [[CLM_ADM.TMP_MAPSEGMENT_MOBILE]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK |
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
- → [[CLM_ADM.ADM_MAPSEGMENT_MOBILE]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK |
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

