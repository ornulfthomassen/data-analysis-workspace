# KIM_BLANK_ORDER_RANK

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure iterates through a list of order IDs from the 'dup_order_rank_2017' table/view. For each order ID, it updates the 'CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT' table, setting the 'ORDER_RANK' column to NULL for records matching the order ID and having a 'contact_date_key' on or after '20170101'. The procedure commits changes in batches of 10,000 records.

## Data Sources (Inputs)
- ← [[dup_order_rank_2017]]
| Column Name |
|---|
| order_id |
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| ORDER_ID |
| contact_date_key |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| ORDER_RANK |

