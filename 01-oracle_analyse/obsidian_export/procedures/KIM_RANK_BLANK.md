# KIM_RANK_BLANK

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure iterates through distinct order IDs from the `kim_campaign_detail_fact` table, identified within a specified contact date range (`P_FROM_CONTACT_DT_KEY` to `P_TO_CONTACT_DT_KEY`) and where an `order_rank` currently exists. For each such `order_id`, it updates the `ORDER_RANK` to NULL and sets a fixed value for `seq_id_upd` in the `CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT` table. This update is applied to records associated with that specific `order_id` and having a `contact_date_key` greater than '20180101', effectively un-ranking or blanking out the order rank for these specific orders.

## Data Sources (Inputs)
- ← [[kim_campaign_detail_fact]]
| Column Name |
|---|
| order_id |
| contact_date_key |
| order_rank |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| ORDER_RANK |
| seq_id_upd |

