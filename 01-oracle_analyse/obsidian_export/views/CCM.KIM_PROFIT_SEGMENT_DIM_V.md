# KIM_PROFIT_SEGMENT_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view creates a dimension for customer profitability segments. It combines segment details with model information, specifically filtering for models named 'Kundelønnsomhet' (Customer Profitability).

## Data Sources (Inputs)
- ← [[CCDW_SEGMENT.SEGMENT]]
| Column Name |
|---|
| SEGMENT_ID |
| SEGMENT_NAME |
| SEGMENT_CRITERIA |
| SEGMENT_COMMENT |
| MODEL_ID |

- ← [[CCDW_SEGMENT.MODEL]]
| Column Name |
|---|
| MODEL_ID |
| MODEL_NAME |
| MODEL_DESC |


