# KIM_UPDATE_ORDER_HIT

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure iterates through a join of order line details and campaign detail facts. For each record retrieved, it updates the `CAMPAIGN_HIT_TYPE_KEY` in the `CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT` table, setting it to the value found in `galaxy.order_line_detail_fact_mv` for the corresponding `CONTACT_KEY`. It includes periodic commits to manage transaction size.

## Data Sources (Inputs)
- ← [[galaxy.order_line_detail_fact_mv]]
| Column Name |
|---|
| CAMPAIGN_HIT_TYPE_KEY |
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
| CAMPAIGN_HIT_TYPE_KEY |
| CONTACT_KEY |

