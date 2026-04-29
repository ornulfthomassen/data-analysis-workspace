# KIM_ORDERBLANK_94

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Iterates through specific campaign detail records based on predefined criteria, and for each matching record's contact, it updates multiple order-related columns within the KIM_CAMPAIGN_DETAIL_FACT table to default null or -1 values, effectively 'blanking out' order information. Changes are committed periodically and at the end.

## Data Sources (Inputs)
- ← [[kim_campaign_detail_fact]]
| Column Name |
|---|
| contact_key |
| ORDER_DEALER_KEY |
| order_rank_group_key |
| contact_date_key |
| source_system_key |
- ← [[KIM_DEALER_DIM_V]]
| Column Name |
|---|
| dealer_key |
| SOURCE_DEALER_ID |

## Target Tables (Outputs)
- → [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| ORDER_ID |
| BINDING_BENEFIT_DESC |
| ORDER_BINDING_PRODUCT_KEY |
| ORDER_DEALER_KEY |
| ORDER_DT_KEY |
| ORDER_FROM_PRODUCT_KEY |
| ORDER_HANDSET_KEY |
| ORDER_LINE_TYPE_KEY |
| ORDER_MATCH_KEY |
| ORDER_RANK |
| ORDER_SERVICE_PROVIDER_KEY |
| ORDER_RANK_GROUP_KEY |
| ORDER_SOURCE_SYSTEM_KEY |
| ORDER_STATUS_KEY |
| ORDER_TO_PRODUCT_KEY |

