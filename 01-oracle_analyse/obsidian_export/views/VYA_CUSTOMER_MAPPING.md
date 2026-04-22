# VYA_CUSTOMER_MAPPING

**Schema:** `CCM` | **Type:** `View`

## Description
Transforms and filters customer mapping data from the `ADM_CUSTOMER_MAPPING` table. It provides the original numeric `KURT_ID` and `CUSTOMER_SK`, along with character representations of both (`KURT_ID_CHAR` and `CUSTOMER_SK`). Records are filtered to include only those where `KURT_ID` is a positive value.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]

