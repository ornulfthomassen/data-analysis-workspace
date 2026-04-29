# PI_SK_MAP_UP

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a distinct mapping view between main number identifiers (main_number_sk) and subscription identifiers (subscription_sk) using historical subscription master data, including a main number rank.

## Data Sources (Inputs)
- ← [[clm_adm.adm_subscription_master_hist]]
| Column Name |
|---|
| main_number_sk |
| subscription_id |
| main_number_rank |

