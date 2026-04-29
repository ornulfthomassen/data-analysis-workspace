# VYA_ORDER_STATUS_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a dimension view for order statuses by selecting existing status attributes and deriving a standardized 'STATUS_CD' based on business rules related to 'MOBILE' business area and various status categories and types, intended for use in Viya.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_STATUS_DIM_MV]]
| Column Name |
|---|
| ORDER_STATUS_KEY |
| ORDER_STATUS_NAME |
| ORDER_STATUS_DESC |
| ORDER_STATUS_CATEGORY_CODE |
| ORDER_STATUS_CATEGORY_DESC |
| ORDER_STATUS_TYPE_CODE |
| ORDER_STATUS_TYPE_DESC |
| SOURCE_SYSTEM_STATUS_CODE |
| BUSINESS_AREA_NAME |

