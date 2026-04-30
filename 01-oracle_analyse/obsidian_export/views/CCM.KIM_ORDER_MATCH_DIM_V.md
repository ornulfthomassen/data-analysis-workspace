# KIM_ORDER_MATCH_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a dimension view `KIM_ORDER_MATCH_DIM_V` by selecting all columns from `KIM_ORDER_MATCH_DIM`. It standardizes certain dimension attributes (`ORDER_MATCH_NAME`, `ORDER_MATCH_DESC`, `ORDER_MATCH_GROUP`, `ORDER_MATCH_SUB_GROUP`) by replacing NULL values with '-1' and explicitly casting them to VARCHAR2.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_ORDER_MATCH_DIM]]
| Column Name |
|---|
| ORDER_MATCH_KEY |
| ORDER_MATCH_NAME |
| ORDER_MATCH_DESC |
| ORDER_MATCH_GROUP |
| ORDER_MATCH_RANK |
| ORDER_MATCH_SUB_GROUP |


