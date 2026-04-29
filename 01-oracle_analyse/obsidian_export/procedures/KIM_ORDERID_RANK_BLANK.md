# KIM_ORDERID_RANK_BLANK

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Identifies records in 'CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT' where an 'order_id' has multiple 'order_rank=1' entries within a user-specified date range (START_ORDER_DATE_KEY to END_ORDER_DATE_KEY). For these identified 'order_id's, the procedure updates the 'ORDER_RANK' to NULL and sets 'seq_id_upd' to a specific hardcoded value, but only for records with 'contact_date_key' greater than 20170101. This process effectively corrects duplicate rank entries for certain orders.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
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

