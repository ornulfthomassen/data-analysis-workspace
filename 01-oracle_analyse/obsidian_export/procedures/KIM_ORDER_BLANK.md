# KIM_ORDER_BLANK

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Blanks out (updates to default/null values) specific order-related columns in the KIM_CAMPAIGN_DETAIL_FACT table for records matching criteria such as a specified date key, measure type (1), order match key (> 0), and source system keys (58 or 63). For each record updated, the procedure first archives the original values of the relevant columns, along with a timestamp and update count, into a dynamically created tracking table (e.g., BCK_KCDF_ORDER_B_YYMMDD_YYMMDD).

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| SOURCE_SYSTEM_KEY |
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
| CONTACT_DATE_KEY |
| MEASURE_TYPE |

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
- → [[V_SPORINGSTABELL]]
| Column Name |
|---|
| DTTM |
| UPDATED |
| CONTACT_KEY |
| SOURCE_SYSTEM_KEY |
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

