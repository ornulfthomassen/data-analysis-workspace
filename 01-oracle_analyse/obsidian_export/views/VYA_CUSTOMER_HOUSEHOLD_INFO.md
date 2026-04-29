# VYA_CUSTOMER_HOUSEHOLD_INFO

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates and transforms customer and household data, providing detailed household-level statistics (e.g., age distribution, gender counts, address details) and service subscription flags, linked by a customer key.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_CUSTOMER]]
| Column Name |
|---|
| KURT_ID |
| HOUSEHOLD_ID |
| AGE |
| GENDER |
| CUSTOMER_TYPE_CD |
| CUSTOMER_STATUS_CD |
| EMAIL_ADRESSE |
| SMS_MOBIL |
- ← [[CLM_CCM.CCM_CUSTOMER_CONTACT_INFO]]
| Column Name |
|---|
| KURT_ID |
| STREET_POSTAL_CODE |
| STREET_POSTAL_ADDRESS |
- ← [[CLM_CCM.CCM_HOUSEHOLD_INFO]]
| Column Name |
|---|
| HOUSEHOLD_ID |
| ANTALL_I_HUSSTAND |
| POSTNR |
| KOMMUNENR |
| GRUNNKRETS_NR |
| BORETTSLAGSID |
| BYGNINGSTYPE_NR |
| BOLIGTYPE |
| FIXED_TALE |
| TV |
| FIXED_INTERNETT_DSL |
| FIXED_INTERNETT_WIMAX |
| FIXED_INTERNETT_FIBER |
| FIXED_INTERNETT_DIALUP |
| FRISURF |
| MOBIL_INTERNETT |
| MOBIL_TALE |
| FRI_FAMILIE |
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |

