# V_JOE_SWAP_IMEI

**Schema:** `CCM` | **Type:** `View`

## Description
Combines device (IMEI) and subscription-related information, including details on swap agreements and various insurance policies ('fors'), with customer mapping data to link devices and subscriptions to specific customer records and household IDs.

## Data Sources (Inputs)
- ← [[ADHOC_BS.AH_2006_SAMMEN]]
| Column Name |
|---|
| imei |
| device_manufacturer_short |
| device_marketing_name |
| mnd_var |
| subscription_key |
| prim_product_desc |
| swap_avtale |
| puss_fors |
| mob_pad_fors |
| pluss_fors_etter_swap |
| pluss_fors_swap_slutt |
| skjerm_fors_swap_slutt |
| swap_pluss_fors |
| swap_skjerm_fors |
| clm_descr |
| household_id |
| owner_customer_key |
- ← [[clm_adm.adm_customer_mapping]]
| Column Name |
|---|
| customer_sk |
| kurt_id |

