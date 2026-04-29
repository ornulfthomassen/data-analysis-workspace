# HS_CLUSTER_ANALYSE

**Schema:** `CCM` | **Type:** `View`

## Description
This view combines customer cluster analysis data with subscription master history, filtering subscriptions active around April 2019, to provide a distinct set of subscription, customer, product, and historical metric details for analysis.

## Data Sources (Inputs)
- ← [[crm_analyse.hs_fleksi_clusteranal_1904]]
| Column Name |
|---|
| mpp_main_id_sk |
| mpp_customer_sk_user |
| cu_customer_sk_owner |
| fleksi_segment |
| periode |
| mpp_product_name |
| mpp_no_days_active |
| mpp_no_days_prod |
| MB_AVG_LAST12 |
| MB_STDAV_LAST12 |
- ← [[clm_adm.adm_subscription_master_hist]]
| Column Name |
|---|
| subscription_id |
| MAIN_NUMBER_SK |
| original_start_date |
| end_date |

