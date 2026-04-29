# VYA_FTV_KAS_CUST_SUB_KEY

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies and consolidates broadband ('Bredbånd') and TV subscription keys and KAS subscriber numbers for customers. It filters for subscriptions from the 'KAS' source system where the sub-product is the primary product, and only includes customers who have exactly one distinct subscription key for a given subscription category (broadband or TV). The view pivots these details, providing separate columns for broadband and TV subscription keys and KAS subscriber numbers.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
| Column Name |
|---|
| OWNER_CUSTOMER_KEY |
| SUBSCRIPTION_KEY |
| SUB_PRODUCT_KEY |
| PRIM_PRODUCT_KEY |
- ← [[GALAXY.SUBSCRIPTION_DIM]]
| Column Name |
|---|
| SOURCE_SUBSCR_ID_1 |
| SUBSCRIPTION_KEY |
| MARKET_AREA_DESC |
| SUBSCR_CATEGORY_NAME |
| SOURCE_SYSTEM_NAME |
| CURRENT_STATUS |

