# VYA_CCM_CUSTOMER_TMP

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a temporary view to extract customer date of birth (DOB) and customer_SK for calculating customer age at order date. This view is marked as temporary and intended for deletion.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_CUSTOMER_V]]
| Column Name |
|---|
| DATE_OF_BIRTH |
| LOAD_DTTM |
| KURT_ID |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |

