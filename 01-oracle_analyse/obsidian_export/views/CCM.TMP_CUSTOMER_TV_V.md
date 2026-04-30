# TMP_CUSTOMER_TV_V

**Schema:** `CCM` | **Type:** `View`

## Description
Joins customer information from `CCM_CUSTOMER_INFO_2` with customer mapping data from `ADM_CUSTOMER_MAPPING_V` using a common `KURT_ID` to retrieve `CUSTOMER_KEY` and `CU_NO_TV_FTV`.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_CUSTOMER_INFO_2]]
| Column Name |
|---|
| CU_NO_TV_FTV |
| KURT_ID |

- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
| Column Name |
|---|
| CUSTOMER_KEY |
| KURT_ID |


