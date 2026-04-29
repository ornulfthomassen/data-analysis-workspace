# VYA_AGREEMENT_SPILLBKV

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates agreement details, product information, and customer mapping. It enriches agreement data with product names and descriptions, and assigns a customer_sk (defaulting to -1 if not found) based on a customer mapping. The view specifically filters for agreements related to a predefined list of product keys.

## Data Sources (Inputs)
- ← [[GALAXY.AGREEMENT_DETAIL_FACT]]
| Column Name |
|---|
| AGREEMENT_KEY |
| AGREEMENT_OFFER_KEY |
| AGREEMENT_PRODUCT_KEY |
| AGREE_START_DT_KEY |
| AGREE_end_DT_KEY |
| AGREE_PRODUCT_QUANTITY |
| AGREE_MEMBER_PRODUCT_QUANTITY |
| AGREE_USER_PRODUCT_QUANTITY |
| AGREE_OWNER_CUST_KEY |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| product_name |
| PRODUCT_DESC |
| product_key |
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
| Column Name |
|---|
| CUSTOMER_SK |
| kurt_id |

