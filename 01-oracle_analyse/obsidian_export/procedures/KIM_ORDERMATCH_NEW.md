# KIM_ORDERMATCH_NEW

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure processes distinct order line campaign ranking data from a temporary table (`CRM_ANALYSE.ORDER_LINE_CAMPAIGN_RANK_TMP`) and uses this data to update corresponding records in the `CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT` table based on the `CONTACT_KEY`. It updates various order-related and campaign-specific attributes in batches.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ORDER_LINE_CAMPAIGN_RANK_TMP]]
| Column Name |
|---|
| CONTACT_KEY |
| ORDER_RANK |
| ORDER_MATCH_KEY |
| ORDER_DT_KEY |
| ORDER_STATUS_DT_KEY |
| ORDER_ID |
| ORDER_LINE_TYPE_KEY |
| ORDER_FROM_PRODUCT_KEY |
| ORDER_TO_PRODUCT_KEY |
| ORDER_BINDING_PRODUCT_KEY |
| ORDER_DEALER_KEY |
| ORDER_SOURCE_SYSTEM_KEY |
| ORDER_HANDSET_KEY |
| BINDING_BENEFIT_DESC |
| ORDER_RANK_GROUP_KEY |
| SALES_MATRIX |
| seq_id_upd |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| ORDER_RANK |
| ORDER_MATCH_KEY |
| ORDER_DT_KEY |
| ORDER_STATUS_DT_KEY |
| ORDER_ID |
| ORDER_LINE_TYPE_KEY |
| ORDER_FROM_PRODUCT_KEY |
| ORDER_TO_PRODUCT_KEY |
| ORDER_BINDING_PRODUCT_KEY |
| ORDER_DEALER_KEY |
| ORDER_SOURCE_SYSTEM_KEY |
| ORDER_HANDSET_KEY |
| BINDING_BENEFIT_DESC |
| ORDER_RANK_GROUP_KEY |
| SALES_MATRIX |
| seq_id_upd |

