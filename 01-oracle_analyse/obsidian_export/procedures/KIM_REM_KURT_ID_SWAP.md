# KIM_REM_KURT_ID_SWAP

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Iterates through records in `KIM_CAMPAIGN_DETAIL_FACT_EXT` where `SWAP_MATCH` is 'KURT_ID    ', and for each such record, it resets (sets to NULL) various swap-related columns including `SWAP_PRODUCT_KEY`, `SWAP_DTTM`, `SWAP_DEALER_KEY`, `SWAP_ORDER_ID`, `SWAP_MATCH`, and `SWAP_RANK` in the same table. The procedure commits changes periodically.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT_EXT]]
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

