# P_ADM_MAP2_SEGMENT_LAST

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure calculates the most recent MAP2 segment and period for each customer (KURT_ID) based on historical segment data from the past 23 months. It first populates a temporary table with these aggregated results, then drops and recreates a permanent summary table (`ADM_MAP2_SEGMENT_LAST`) by selecting from the temporary table, adding a formatted segment description. Finally, it creates an index on the permanent table and collects its statistics.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MAP2_SEGMENT_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| MAP2_SEGMENT_ID |
| CUSTOMER_SK |
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| RELATIVE_MONTH |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |
- ← [[TMP_MAP2_SEGMENT_LAST]]
| Column Name |
|---|
| KURT_ID |
| LAST_PERIOD_MONTH_KEY |
| LAST_MAP2_SEGMENT_ID |

## Target Tables (Outputs)
- → [[TMP_MAP2_SEGMENT_LAST]]
| Column Name |
|---|
| KURT_ID |
| LAST_PERIOD_MONTH_KEY |
| LAST_MAP2_SEGMENT_ID |
- → [[ADM_MAP2_SEGMENT_LAST]]
| Column Name |
|---|
| KURT_ID |
| LAST_MAP2_PERIOD_MONTH_KEY |
| LAST_MAP2_SEGMENT_ID |
| LAST_MAP2_SEGMENT |

