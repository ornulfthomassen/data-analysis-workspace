# KIM_UPDATE_ORDER_DATE

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure updates order source system keys and order date keys in the `KIM_CAMPAIGN_DETAIL_FACT` table. It achieves this by joining `KIM_CAMPAIGN_DETAIL_FACT` with `ORDER_LINE_DETAIL_FACT_MV` based on matching order IDs and a positive order match key, then applying the fetched source system and date keys to the campaign fact table for the corresponding contact.

## Data Sources (Inputs)
- ← [[galaxy.order_line_detail_fact_mv]]
| Column Name |
|---|
| SOURCE_SYSTEM_KEY |
| ORDER_DT_KEY |
| SOURCE_ORDER_ID |
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| ORDER_ID |
| ORDER_MATCH_KEY |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| ORDER_SOURCE_SYSTEM_KEY |
| ORDER_DT_KEY |

