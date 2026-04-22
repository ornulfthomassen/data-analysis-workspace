# V_SAS_CONTACT_RAW

**Schema:** `CCM` | **Type:** `View`

## Description
This view extracts raw customer contact history data, enriching it with details about dynamic treatment attributes, external presented information, and contact responses. It filters records to include contacts from the beginning of the previous month up to the current date, specifically for campaigns 'C1', 'C3', and 'C8', and only when a trigger ID is present. The view provides a detailed, raw dataset for further analysis related to customer interactions and campaign performance.

## Data Sources (Inputs)
- ← [[clm_cdm.ci_cust_contact_history_sdw]]
- ← [[clm_cdm.ci_dynamic_treatment_attribute]]
- ← [[clm_cdm.ci_dynamic_treatment_attr_ext]]
- ← [[clm_cdm.ci_cust_pres_treat_history]]
- ← [[CLM_CDM.V_RTDM_CH_RH]]
- ← [[clm_cdm.ci_response]]

