# VYA_CCM_CUSTOMER_TMP

**Schema:** `CCM` | **Type:** `View`

## Description
This view is designed to extract customer-related information, specifically a customer SKU (CUSTOMER_SK), date of birth (DOB), and load timestamp (LOAD_DTTM). Its primary purpose, as indicated by the comments, is to temporarily provide customer Date of Birth data to facilitate the calculation of customer age at the order date. The view joins `CCM_CUSTOMER_V` with `ADM_CUSTOMER_MAPPING` on `KURT_ID` to achieve this. It is explicitly noted as a temporary view to be deleted soon.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_CUSTOMER_V]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]

