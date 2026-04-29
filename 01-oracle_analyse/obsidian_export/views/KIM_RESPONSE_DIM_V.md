# KIM_RESPONSE_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a dimension view for CRM response data by selecting all columns from the base response dimension table, applying null handling (replacing nulls with '-1') and explicit casting to specific VARCHAR2 lengths for several key attributes (RESPONSE_CD, RESPONSE_GROUP, RESPONSE_NM, CURRENT_STATUS).

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]
| Column Name |
|---|
| RESPONSE_KEY |
| RESPONSE_CD |
| RESPONSE_GROUP |
| RESPONSE_NM |
| CURRENT_STATUS |
| START_DATE |
| END_DATE |
| RESPONSE_RANK |
| SOURCE_SYSTEM_KEY |

