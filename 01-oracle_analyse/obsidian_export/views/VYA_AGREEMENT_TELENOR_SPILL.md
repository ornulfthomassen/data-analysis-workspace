# VYA_AGREEMENT_TELENOR_SPILL

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides detailed agreement information by joining agreement fact data with product dimensions and customer mappings. It includes product name, a derived customer surrogate key, and various agreement-related keys and quantities, filtered for specific product keys.

## Data Sources (Inputs)
- ← [[GALAXY.AGREEMENT_DETAIL_FACT]]
| Column Name |
|---|
| AGREEMENT_OFFER_KEY |
| AGREEMENT_PRODUCT_KEY |
| AGREE_START_DT_KEY |
| AGREE_END_DT_KEY |
| AGREE_PRODUCT_QUANTITY |
| AGREE_MEMBER_PRODUCT_QUANTITY |
| AGREE_USER_PRODUCT_QUANTITY |
| AGREE_OWNER_CUST_KEY |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| product_name |
| product_key |
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
| Column Name |
|---|
| CUSTOMER_SK |
| kurt_id |

