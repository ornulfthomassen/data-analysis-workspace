# KIM_ORDER_BLANK_FRM_BKP

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Iterates through contact keys from a 2016 backup table and, for each contact key, updates a set of order-related columns in the KIM_CAMPAIGN_DETAIL_FACT table to default or null values for records within the year 2016. This essentially 'blanks out' or neutralizes specific order details for these contacts and dates.

## Data Sources (Inputs)
- ← [[KIM_CROSSKPI_MATCH_2016_BKP]]
| Column Name |
|---|
| CONTACT_KEY |
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
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

