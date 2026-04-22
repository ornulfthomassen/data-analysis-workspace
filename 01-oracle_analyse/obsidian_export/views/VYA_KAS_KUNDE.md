# VYA_KAS_KUNDE

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates and standardizes customer information, including personal details, address information, financial data (saldo, credit limit), contract details, and status information. It also integrates customer data with an analytical customer mapping system, deriving a 'CUSTOMER_SK' and cleaning/transforming several customer attributes (e.g., KUNDE_TYPE to uppercase, FODSELSDATO_DATO to FODSELSAAR). The view filters out customer types marked as 'X'.

## Data Sources (Inputs)
- ← [[KAS.KUNDE]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]

