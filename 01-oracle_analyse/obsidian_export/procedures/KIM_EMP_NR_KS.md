# KIM_EMP_NR_KS

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure iterates through customer contact history, cell package information, and campaign detail facts. It extracts a specific identifier (likely an employee number) from the 'EXTERNAL_CONTACT_INFO_ID1' field of the contact history table, based on various filtering conditions and regular expression patterns. For each matching record, it updates the 'CONN_ID' column in the 'KIM_CAMPAIGN_DETAIL_FACT' table with the extracted identifier, using the 'CONTACT_KEY' as a join condition. The procedure commits changes periodically.

## Data Sources (Inputs)
- ← [[RTDM_CDM.CI_CUST_CONTACT_HISTORY]]
| Column Name |
|---|
| EXTERNAL_CONTACT_INFO_ID1 |
| CELL_PACKAGE_SK |
| CU_KURT_ID_OWNER |
| CONTACT_DTTM |
- ← [[RTDM_CDM.CI_CELL_PACKAGE]]
| Column Name |
|---|
| CELL_PACKAGE_SK |
| CHANNEL_CD |
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| CELL_PACKAGE_SK |
| KURT_ID_OWNER |
| CONTACT_DTTM |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONN_ID |
| CONTACT_KEY |

