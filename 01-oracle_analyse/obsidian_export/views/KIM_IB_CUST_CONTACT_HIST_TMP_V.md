# KIM_IB_CUST_CONTACT_HIST_TMP_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `KIM_IB_CUST_CONTACT_HIST_TMP_V`, combines customer contact history with package, treatment, campaign, and communication details. It extracts subscription IDs and main phone numbers from custom user-defined fields (UDFs) associated with treatments and maps them to actual subscription records from the `CCDW` schema. The view specifically filters for contact records after a certain date ('01.01.2014') and excludes records that have already been processed into the `CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT` table. It also assigns a ranking (`RANGERING`) to contact records based on various attributes, likely for prioritization or identifying unique interactions for further analysis or data loading.

## Data Sources (Inputs)
- ← [[RTDM_CDM.CI_CUST_CONTACT_HISTORY]]
- ← [[RTDM_CDM.CI_PACKAGE_X_TREATMENT]]
- ← [[RTDM_CDM.CI_DYNAMIC_TREATMENT_ATTRIBUTE]]
- ← [[RTDM_CDM.CI_CELL_PACKAGE]]
- ← [[RTDM_CDM.CI_TREATMENT_CHAR_UDF]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]

