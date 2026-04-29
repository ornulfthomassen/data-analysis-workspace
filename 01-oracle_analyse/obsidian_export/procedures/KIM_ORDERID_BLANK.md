# KIM_ORDERID_BLANK

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Identifies records in the `kim_campaign_detail_fact` table where the `order_id` is duplicated for entries with `order_rank = 1` and `contact_date_key` greater than '20170601'. For these identified `order_id`s, it updates the `ORDER_RANK` column to `NULL` and the `seq_id_upd` column to `999801` in the `CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT` table.

## Data Sources (Inputs)
- ← [[kim_campaign_detail_fact]]
| Column Name |
|---|
| order_id |
| order_rank |
| contact_date_key |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| ORDER_RANK |
| seq_id_upd |

