# V_SAS_CONTACT_RAW

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates customer contact history with dynamic treatment attributes, presented treatment details, and response information. It filters for contacts within the last full month plus the current month, specifically for campaigns 'C8', 'C1', 'C3', and only includes records where a trigger ID is present. The output provides a raw dataset for SAS analytics related to customer interactions.

## Data Sources (Inputs)
- ← [[CLM_CDM.CI_CUST_CONTACT_HISTORY_SDW]]
| Column Name |
|---|
| KURT_ID |
| contact_dttm |
| cell_package_sk |
| package_hash_val |
| contact_dt |

- ← [[CLM_CDM.CI_DYNAMIC_TREATMENT_ATTRIBUTE]]
| Column Name |
|---|
| cell_package_sk |
| package_hash_val |
| treatment_hash_val |

- ← [[CLM_CDM.CI_DYNAMIC_TREATMENT_ATTR_EXT]]
| Column Name |
|---|
| campaign_id |
| main_number |
| subscription_id |
| trigger_id |
| dialogue_id |
| treatment_hash_val |

- ← [[CLM_CDM.CI_CUST_PRES_TREAT_HISTORY]]
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

- ← [[CLM_CDM.CI_RESPONSE]]
| Column Name |
|---|
| response_nm |
| response_cd |


