# VYA_CDC_ADDRESS_LINK

**Schema:** `CCM` | **Type:** `View`

## Description
This view links address details from the CDC.ADDRESS_LINK table to master customer records in CDC.MASTER_CUSTOMER, and further to customer mapping information in CLM_ADM.ADM_CUSTOMER_MAPPING. It filters records based on customer mapping status ('EKSKUNDE', 'KUNDE') and a complex date logic involving the address's validity period and various customer start dates from the mapping table, effectively providing a filtered and joined view of customer address links with an associated customer surrogate key.

## Data Sources (Inputs)
- ← [[CDC.ADDRESS_LINK]]
| Column Name |
|---|
| ADDRESS_LINK_ID |
| ADDRESS_TYPE_LINK_ID |
| CONTACT_ROLE_ID |
| COMM_PURPOSE_ID |
| COMM_PURP_GROUP_ID |
| ADDRESS_LOCATION_ID |
| PROSPECT_CUST_ID |
| PARTNER_ID |
| PREFERRED_ADDRESS |
| ARRANGEMENT_CUSTOMER_ROLE_ID |
| ENTITY_ROLE_ID |
| ENTITY_ROLE_TYPE_ID |
| VALID_FROM_DATE |
| VALID_TO_DATE |
| INFO_REG_USER_NAME |
| INFO_REG_APPL_NAME |
| INFO_REG_DATE |
| INFO_CHG_USER_NAME |
| INFO_CHG_APPL_NAME |
| INFO_CHG_DATE |
| INFO_IS_DELETED |
| MASTER_ID |
- ← [[CDC.MASTER_CUSTOMER]]
| Column Name |
|---|
| MASTER_ID |
| KURT_ID |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |
| MAP_STATUS |
| OWNER_START_DATE_ORIG |
| USER_START_DATE_ORIG |
| OWNER_START_DATE |
| USER_START_DATE |

