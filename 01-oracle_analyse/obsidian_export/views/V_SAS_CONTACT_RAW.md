# V_SAS_CONTACT_RAW

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates customer contact history with dynamic treatment attributes, presented treatment details, and response information. It filters for contacts within the last full month plus the current month, specifically for campaigns 'C8', 'C1', 'C3', and only includes records where a trigger ID is present. The output provides a raw dataset for SAS analytics related to customer interactions.

## Data Sources (Inputs)
- ← [[clm_cdm.ci_cust_contact_history_sdw]]
| Column Name |
|---|
| KURT_ID |
| contact_dttm |
| cell_package_sk |
| package_hash_val |
| contact_dt |
- ← [[clm_cdm.ci_dynamic_treatment_attribute]]
| Column Name |
|---|
| cell_package_sk |
| package_hash_val |
| treatment_hash_val |
- ← [[clm_cdm.ci_dynamic_treatment_attr_ext]]
| Column Name |
|---|
| campaign_id |
| main_number |
| subscription_id |
| trigger_id |
| dialogue_id |
| treatment_hash_val |
- ← [[clm_cdm.ci_cust_pres_treat_history]]
| Column Name |
|---|
| external_presented_info_id1 |
| cell_package_sk |
| treatment_hash_val |
| presented_treatment_hist_dttm |
- ← [[CLM_CDM.V_RTDM_CH_RH]]
| Column Name |
|---|
| treatment_hash_val |
| contact_dttm |
| response_cd |
- ← [[clm_cdm.ci_response]]
| Column Name |
|---|
| response_nm |
| response_cd |

