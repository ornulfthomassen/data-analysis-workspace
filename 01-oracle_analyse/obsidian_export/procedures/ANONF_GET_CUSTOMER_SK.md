# ANONF_GET_CUSTOMER_SK

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Retrieves or determines a customer's surrogate key (CUSTOMER_SK) based on a given KURT_ID. It validates the KURT_ID against the KURT.KURT table and then checks the ANON_ADM_CUSTOMER_MAPPING table. Based on the mapping status ('KUNDE' or 'EKSKUNDE'), it either returns the existing CUSTOMER_SK or calls other functions to reactivate it. It includes extensive error handling for various scenarios like non-existent, duplicate, or unmapped KURT_IDs, and unhandled mapping statuses.

## Data Sources (Inputs)
- ← [[KURT.KURT]]
| Column Name |
|---|
| KID |
- ← [[ANON_ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |
| MAP_STATUS |

