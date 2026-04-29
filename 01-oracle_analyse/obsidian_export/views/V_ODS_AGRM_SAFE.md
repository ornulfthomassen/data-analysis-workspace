# V_ODS_AGRM_SAFE

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and filters agreement and product details, specifically for 'SAFE' or 'Sikker ID' products, from operational data store (ODS) mobile views and customer mapping data. It joins agreement information with specific offer details and customer mapping to provide a comprehensive view, including flags for active agreements and products.

## Data Sources (Inputs)
- ← [[clm_ccm.v_ods_agrmt_mob]]
| Column Name |
|---|
| agreement_id |
| src_agrm_agreement_offer_id |
| agreement_product_name |
| agreement_status |
| agreement_start_date |
| agreement_end_date |
- ← [[clm_ccm.v_ods_agrmt_offer_mob_safety]]
| Column Name |
|---|
| agreement_id |
| src_agrm_agreement_offer_id |
| product_status |
| product_name |
| product_start_date |
| product_end_date |
| kurt_id |
- ← [[clm_adm.adm_customer_mapping]]
| Column Name |
|---|
| customer_sk |
| kurt_id |

