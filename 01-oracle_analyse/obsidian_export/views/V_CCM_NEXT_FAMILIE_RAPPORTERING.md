# V_CCM_NEXT_FAMILIE_RAPPORTERING

**Schema:** `CCM` | **Type:** `View`

## Description
This view generates a multi-level report on 'Next Familie' mobile subscriptions. It aggregates subscription data by monthly period and product, providing total counts for adult ('Voksen') and under-18 ('Under 18') family members, as well as the total number of 'Next Familie' subscriptions. The report includes three levels of detail: an overall summary, subtotals per product, and a detailed breakdown by product and specific family member type (adult/under-18), filtered for specific product attributes and discount types associated with 'Next Familie' plans.

## Data Sources (Inputs)
- ← [[CLM_ADM.STOCK_MOBILE_HISTORY_MONTH_DET]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| PRODUCT_KEY |
| CUSTOMER_SK_OWNER |
| DISCOUNT_PRODUCT_KEY |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME |
| DRM_COMMON_PRODUCT_AREA |
| DRM_COMMON_TECHNOLOGY |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_REPORTING |
| PRODUCT_FAMILY_NAME |

