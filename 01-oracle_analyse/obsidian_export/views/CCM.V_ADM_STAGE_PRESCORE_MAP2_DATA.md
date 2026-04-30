# V_ADM_STAGE_PRESCORE_MAP2_DATA

**Schema:** `CCM` | **Type:** `View`

## Description
The view `V_ADM_STAGE_PRESCORE_MAP2_DATA` consolidates customer-related data for pre-scoring or analytical purposes. It combines administrative scoring metrics from `ADM_SCORING_TABLE_CUST` with customer demographics (age), mobile postpaid product tenure (calculated from subscription start dates and product types), and other customer information from various `CLM_CCM` tables. It calculates the number of days a customer has had a postpaid mobile product, handling cases where there might be no such products.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_SCORING_TABLE_CUST]]
| Column Name |
|---|
| KURT_ID |
| CU_U_MAIN_NO_DAYS_ACTIVE |
| CU_U_NET_REV_AVG_3MO |
| CU_U_MB_AVG_3MO |

- ← [[CLM_CCM.CCM_CUSTOMER]]
| Column Name |
|---|
| KURT_ID |
| AGE |

- ← [[CLM_CCM.CCM_CUSTOMER_INFO_2]]
| Column Name |
|---|
| KURT_ID |
| CU_NO_MPP |

- ← [[CLM_CCM.CCM_SUBSCRIPTION_V]]
| Column Name |
|---|
| OWNER_KURT_ID |
| MAIN_PRODUCT_ID |
| ORIGINAL_START_DATE |

- ← [[CLM_CCM.CCM_PRODUCT_DIM_GALAXY_ADJ]]
| Column Name |
|---|
| PRODUCT_KEY |
| SUBSCRIPTION_TYPE |


