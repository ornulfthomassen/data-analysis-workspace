# KIM_REMOVE_KURT_ID_SWAP

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Iterates through records in the CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_EXT table where the SWAP_MATCH column is 'KURT_ID'. For each matching record, it nullifies several 'SWAP_' related columns (SWAP_PRODUCT_KEY, SWAP_DTTM, SWAP_DEALER_KEY, SWAP_ORDER_ID, SWAP_MATCH, SWAP_RANK) and updates the seq_id_upd column to a fixed value of 77777777. The procedure commits changes in batches of 100,000 records.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_EXT]]
| Column Name |
|---|
| CONTACT_KEY |
| SWAP_MATCH |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_EXT]]
| Column Name |
|---|
| SWAP_PRODUCT_KEY |
| SWAP_DTTM |
| SWAP_DEALER_KEY |
| SWAP_ORDER_ID |
| SWAP_MATCH |
| SWAP_RANK |
| seq_id_upd |

