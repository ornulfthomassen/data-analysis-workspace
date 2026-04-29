# VYA_TALKMORE_CUSTOMER

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a customer data view for the 'Mjøsa' system, transforming and aggregating customer-related metrics from the TALKMORE_MATCH table and enriching it with age group data. Many fields are initialized with default or hardcoded values.

## Data Sources (Inputs)
- ← [[CLM_ADM.TALKMORE_MATCH]]
| Column Name |
|---|
| BIRTHDAY |
| NO_TKM_MPP_USER |
| NO_TKM_MPR_USER |
| NO_TKM_MBB_USER |
| NO_TKM_MPP_BUS_USER |
| NO_TKM_OTHER_USER |
| NO_TKM_MPP_OWNER |
| NO_TKM_MPR_OWNER |
| NO_TKM_MBB_OWNER |
| CUSTOMER_KEY |
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
| Column Name |
|---|
| AGE_GROUP_NAME_8C |
| AGE_GROUP_KEY |

