# KIM_ORDER_BLANK94

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Iterates through contact records in KIM_CAMPAIGN_DETAIL_FACT based on a date condition and updates several order-related columns in the same table to default values (-1 or NULL) for each selected contact.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| contact_key |
| contact_date_key |

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

