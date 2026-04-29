# KIM_FIX_MAIN_NUMBER_OUTBOUND

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure updates the `main_number`, `subscription_key`, and `seq_id_upd` columns in the `KIM_CAMPAIGN_DETAIL_FACT` table. It targets records related to a specific campaign ('C18') from 2017 onwards, where the `main_number` in the extended campaign details (`KIM_CAMPAIGN_DETAIL_FACT_EXT`) is negative. The new `main_number` and `subscription_key` values are sourced from `CI_SUBS_CONTACT_HISTORY` based on linked contact and cell package history. The update is performed in batches of 100,000 records with intermittent commits.

## Data Sources (Inputs)
- ← [[CLM_CDM.CI_CUST_CONTACT_HISTORY_SDW]]
| Column Name |
|---|
| contact_key |
| CELL_PACKAGE_SK |
| KURT_ID |
| CONTACT_DTTM |
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| source_contact_id |
| CONTACT_DATE_KEY |
| CONTACT_KEY |
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_EXT]]
| Column Name |
|---|
| CONTACT_KEY |
| CAMPAIGN_ID |
| main_number |
- ← [[CLM_CDM.CI_CELL_PACKAGE]]
| Column Name |
|---|
| CELL_PACKAGE_SK |
- ← [[clm_cdm.CI_SUBS_CONTACT_HISTORY]]
| Column Name |
|---|
| main_number |
| subscription_id |
| KURT_ID |
| CELL_PACKAGE_SK |
| CONTACT_DTTM |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| main_number |
| subscription_key |
| seq_id_upd |
| contact_key |

