# KIM_COMMUNICATION_UPD

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Iterates through specific campaign detail fact records (CRM_ANALYSE.kim_campaign_detail_fact) that have a COMMUNICATION_KEY of -2 and fall within a defined contact date range. For these records, it updates their COMMUNICATION_KEY in the CRM_ANALYSE.kim_campaign_detail_fact table with a new COMMUNICATION_KEY derived from CRM_ANALYSE.KIM_COMMUNICATION_DIM, based on joins with customer contact history and cell package information.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.kim_campaign_detail_fact]]
| Column Name |
|---|
| CONTACT_KEY |
| source_contact_id |
| source_system_key |
| COMMUNICATION_KEY |
- ← [[CLM_CDM.CI_CUST_CONTACT_HISTORY_sdw]]
| Column Name |
|---|
| contact_key |
| CELL_PACKAGE_SK |
| contact_date_key |
- ← [[CLM_CDM.CI_CELL_PACKAGE]]
| Column Name |
|---|
| CELL_PACKAGE_SK |
| communication_sk |
- ← [[CRM_ANALYSE.KIM_COMMUNICATION_DIM]]
| Column Name |
|---|
| COMMUNICATION_KEY |
| communication_sk |
| source_system_key |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| COMMUNICATION_KEY |
| CONTACT_KEY |

