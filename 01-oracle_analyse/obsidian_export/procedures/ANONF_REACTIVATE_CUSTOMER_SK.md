# ANONF_REACTIVATE_CUSTOMER_SK

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle function, ANONF_REACTIVATE_CUSTOMER_SK, aims to 'reactivate' a customer. It validates a given KURT_ID against the KURT.KURT table and the ANON_ADM_CUSTOMER_MAPPING table. If the KURT_ID exists uniquely and is mapped with a status of 'EKSKUNDE' (likely 'ex-customer' or 'inactive'), the function updates the record in ANON_ADM_CUSTOMER_MAPPING. It changes the MAP_STATUS to 'KUNDE' (customer/active), sets STATUS_DATE, and conditionally updates OWNER_START_DATE, USER_START_DATE, OWNER_NUMBER_OF_TIMES, USER_NUMBER_OF_TIMES, and KURT_ID_UPDATE_DATE based on provided parameters. The function returns the CUSTOMER_SK upon successful reactivation or raises various custom exceptions for validation failures.

## Data Sources (Inputs)
- ← [[KURT.KURT]]
- ← [[ANON_ADM_CUSTOMER_MAPPING]]

## Target Tables (Outputs)
- → [[ANON_ADM_CUSTOMER_MAPPING]]

