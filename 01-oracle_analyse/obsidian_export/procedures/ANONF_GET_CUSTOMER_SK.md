# ANONF_GET_CUSTOMER_SK

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL function, ANONF_GET_CUSTOMER_SK, is designed to retrieve a unique customer surrogate key (CUSTOMER_SK) associated with a given input ID (P_KURT_ID). It performs several validation checks:
1. It first verifies that P_KURT_ID exists uniquely in the 'KURT.KURT' table.
2. It then checks if a mapping for P_KURT_ID already exists in the 'ANON_ADM_CUSTOMER_MAPPING' table. If no mapping is found, it returns -1 (with a commented-out suggestion to call a creation function).
3. It ensures that only a single, unique mapping exists for P_KURT_ID in 'ANON_ADM_CUSTOMER_MAPPING'.
4. Finally, it retrieves the CUSTOMER_SK and its MAP_STATUS from 'ANON_ADM_CUSTOMER_MAPPING'. Based on the status, it either returns the existing CUSTOMER_SK ('KUNDE'), calls another function to reactivate an ex-customer ('EKSKUNDE'), or raises an error for an unrecognized status. The function includes comprehensive error handling for various scenarios, such as missing IDs, duplicate IDs, or unhandled mapping statuses.

## Data Sources (Inputs)
- ← [[KURT.KURT]]
- ← [[ANON_ADM_CUSTOMER_MAPPING]]

