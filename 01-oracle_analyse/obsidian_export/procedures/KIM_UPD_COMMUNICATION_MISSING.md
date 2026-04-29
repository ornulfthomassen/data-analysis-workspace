# KIM_UPD_COMMUNICATION_MISSING

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure iterates through specific campaign detail records that have a placeholder `communication_key` of -1. For each such record, it retrieves the correct `communication_key` by joining `CI_CUST_CONTACT_HISTORY_SDW`, `CI_CELL_PACKAGE`, `KIM_CAMPAIGN_DIM`, and `KIM_COMMUNICATION_DIM` tables. It then updates the `communication_key` in the `KIM_CAMPAIGN_DETAIL_FACT` table with the newly found value. Changes are committed periodically.

## Data Sources (Inputs)
- ← [[CLM_CDM.CI_CUST_CONTACT_HISTORY_SDW]]
| Column Name |
|---|
| CELL_PACKAGE_SK |
| contact_key |
- ← [[CLM_CDM.CI_CELL_PACKAGE]]
| Column Name |
|---|
| CELL_PACKAGE_SK |
| COMMUNICATION_SK |
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| contact_key |
| source_contact_id |
| communication_key |
| campaign_key |
| source_system_key |
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DIM]]
| Column Name |
|---|
| campaign_key |
- ← [[CRM_ANALYSE.KIM_COMMUNICATION_DIM]]
| Column Name |
|---|
| communication_key |
| communication_sk |
| source_system_key |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| communication_key |

