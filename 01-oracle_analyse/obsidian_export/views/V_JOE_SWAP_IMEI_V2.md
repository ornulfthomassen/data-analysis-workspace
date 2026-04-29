# V_JOE_SWAP_IMEI_V2

**Schema:** `CCM` | **Type:** `View`

## Description
This view (`V_JOE_SWAP_IMEI_V2`) exposes specific columns related to IMEI (International Mobile Equipment Identity), device usage, customer information, and various insurance or swap-related flags and details. It acts as a direct projection of data from the `adhoc_bs.ah_2006_sammen_v3` table, likely for specific analytical or reporting purposes concerning IMEI swap operations.

## Data Sources (Inputs)
- ← [[adhoc_bs.ah_2006_sammen_v3]]
| Column Name |
|---|
| imei |
| terminal_use_first_date |
| terminal_use_last_date |
| subscription_key |
| owner_customer_sk |
| prim_product_desc |
| product_agree_drm_com_mrk_prod |
| product_agreement_product_nm |
| product_agreement_product_mod |
| swap_flag |
| clm_descr |
| household_id |
| device_manufacturer_short |
| device_marketing_name |
| hus_ant_imei |
| hus_ant_cust |
| hus_ant_sub |
| hus_swap_avtale |
| hus_swap_pluss_fors |
| hus_mob_pad_fors |
| hus_swap_skjerm_fors |
| hus_pluss_fors_etter_swap |
| hus_pluss_fors |
| hus_pluss_fors_swap_slutt |
| hus_skjerm_fors_swap_slutt |
| cus_ant_imei |
| volume |

