# SAFESEC_CUS_SUB_UP

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies the primary (highest `subscription_key`) 'FKM MOBIL' subscription for each unique customer. It links customer contact phone numbers from `CCM_CUST_CONTACT_PHONE` to customer mappings in `ADM_CUSTOMER_MAPPING`, and then to subscription details in `SUBSCRIPTION_DIM_MV`. It filters for active 'FKM MOBIL' subscriptions and assigns -1 if no matching subscription is found for a customer. The final output provides cast customer and subscription identifiers for reporting purposes.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_CUST_CONTACT_PHONE]]
| Column Name |
|---|
| kurt_id |
| CONTACT_PHN_MOB |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| kurt_id |
| customer_sk |
- ← [[GALAXY.SUBSCRIPTION_DIM_MV]]
| Column Name |
|---|
| subscription_key |
| main_number |
| current_status |
| subscr_category_desc |

