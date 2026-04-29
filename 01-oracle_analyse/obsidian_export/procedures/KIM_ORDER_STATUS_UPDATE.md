# KIM_ORDER_STATUS_UPDATE

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Updates `ORDER_STATUS_KEY`, `ORDER_DT_KEY`, and `ORDER_SOURCE_SYSTEM_KEY` in the `KIM_CAMPAIGN_DETAIL_FACT` table based on matching `ORDER_ID` values from the `GALAXY.ORDER_LINE_DETAIL_FACT_MV` materialized view. The procedure processes records in batches of 1000 with intermediate commits.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| ORDER_ID |
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
| Column Name |
|---|
| ORDER_STATUS_KEY |
| ORDER_DT_KEY |
| SOURCE_SYSTEM_KEY |
| SOURCE_ORDER_ID |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| ORDER_STATUS_KEY |
| ORDER_DT_KEY |
| ORDER_SOURCE_SYSTEM_KEY |
| ORDER_ID |

