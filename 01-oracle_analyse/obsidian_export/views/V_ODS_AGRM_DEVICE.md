# V_ODS_AGRM_DEVICE

**Schema:** `CCM` | **Type:** `View`

## Description
Combines agreement, product, device (IMEI), and customer mapping data, specifically for products named 'Utstyr'. It includes device details, customer ownership, agreement and product status, and calculates flags to indicate active agreements, products, and recent IMEI usage.

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
- ← [[clm_ccm.v_ods_agrmt_offer_mob_device]]
| Column Name |
|---|
| agreement_id |
| src_agrm_agreement_offer_id |
| kurt_id |
| product_status |
| product_name_market |
| product_name |
| product_start_date |
| product_end_date |
| imei_full |
| imei_full_num |
- ← [[clm_adm.adm_customer_mapping]]
| Column Name |
|---|
| kurt_id |
| customer_sk |
- ← [[live.eureka_imei]]
| Column Name |
|---|
| imei |
| terminal_use_first_date |
| terminal_use_last_date |

