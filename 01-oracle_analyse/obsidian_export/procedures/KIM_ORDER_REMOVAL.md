# KIM_ORDER_REMOVAL

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Identifies campaign detail records associated with 'wrong order' or 'duplicate registration' statuses based on specific criteria, and then nullifies a set of order-related attributes within those identified campaign detail records.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| SOURCE_SYSTEM_KEY |
| ORDER_ID |
| ORDER_STATUS_KEY |
- ← [[KIM_ORDER_STATUS_RANK_V]]
| Column Name |
|---|
| ORDER_STATUS_KEY |
| RANK |
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
| Column Name |
|---|
| SOURCE_ORDER_ID |
| ORDER_LINE_ID |
| ORDER_STATUS_REASON_KEY |
- ← [[GALAXY.ORDER_STATUS_REASON_DIM_V]]
| Column Name |
|---|
| ORDER_STATUS_REASON_KEY |
| ORDER_STATUS_REASON_DESC |

## Target Tables (Outputs)
- → [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| ORDER_BINDING_PRODUCT_KEY |
| ORDER_DEALER_KEY |
| ORDER_DT_KEY |
| ORDER_FROM_PRODUCT_KEY |
| ORDER_ID |
| ORDER_LINE_TYPE_KEY |
| ORDER_MATCH_KEY |
| ORDER_RANK |
| ORDER_SERVICE_PROVIDER_KEY |
| ORDER_SOURCE_SYSTEM_KEY |
| ORDER_STATUS_KEY |
| ORDER_TO_PRODUCT_KEY |

