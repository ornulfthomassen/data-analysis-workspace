# KIM_UPD_WRONG_SWAP

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure identifies specific contact records within the `KIM_CAMPAIGN_DETAIL_FACT` table that are associated with a particular product 'swap' agreement type (Telenor Swap nedbetalingsavtale) and also associated with a non-swap product. For these identified contacts, it updates the `ORDER_RANK_GROUP_KEY` and `seq_id_upd` columns in the `CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT` table, applying a hardcoded rank group and a sequence ID.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| ORDER_TO_PRODUCT_KEY |
- ← [[KIM_CAMPAIGN_DETAIL_FACT_EXT]]
| Column Name |
|---|
| CONTACT_KEY |
| PRODUCT_KEY_1 |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_FAMILY_NAME |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| ORDER_RANK_GROUP_KEY |
| seq_id_upd |

