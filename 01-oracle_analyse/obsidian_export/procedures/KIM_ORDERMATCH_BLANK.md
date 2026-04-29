# KIM_ORDERMATCH_BLANK

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Iterates through `KIM_CAMPAIGN_DETAIL_FACT` records that meet specific criteria (source_contact_id and ORDER_match_key) and updates several order-related columns within these records to default 'blank' values (-1 or NULL). The updates are further constrained by a date range (CONTACT_DATE_KEY) provided as input parameters. The procedure processes records in batches of 100,000 before committing.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| source_contact_id |
| ORDER_match_key |
| CONTACT_DATE_KEY |

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

