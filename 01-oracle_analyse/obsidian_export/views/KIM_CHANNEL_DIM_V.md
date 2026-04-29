# KIM_CHANNEL_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view (`KIM_CHANNEL_DIM_V`) provides a standardized and cleaned-up version of channel dimension data. It retrieves all specified columns from the base `KIM_CHANNEL_DIM` table, applying null handling (replacing nulls with '-1') and explicit type casting to VARCHAR2 for several character-based columns to ensure data consistency and length. It also renames the `CHANNEL_COMMON_NM` column from the source table to `CHANNEL` in the view output.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CHANNEL_DIM]]
| Column Name |
|---|
| CHANNEL_KEY |
| SOURCE_SYSTEM_KEY |
| CHANNEL_CD |
| CHANNEL_NM |
| CHANNEL_DESC |
| CHANNEL_COMMON_NM |
| START_DATE |
| END_DATE |
| CURRENT_STATUS |

