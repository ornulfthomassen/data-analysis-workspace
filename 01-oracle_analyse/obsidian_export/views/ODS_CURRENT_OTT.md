# ODS_CURRENT_OTT

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates Over-the-Top (OTT) service usage details for customers, providing the earliest start date, latest end date, and total number of associated user IDs for each customer and service, based on actively linked customer and service records.

## Data Sources (Inputs)
- ← [[COMOYO.USER_SERVICES_SERVICE_SCD]]
| Column Name |
|---|
| START_DATE |
| END_DATE |
| SERVICE_NAME |
| USER_ID |
| CURRENT_RECORD |
- ← [[CLM_CCM.CCM_SERVICES_DIM]]
| Column Name |
|---|
| SERVICE_NAME |
| SERVICE_CD |
| SERVICE_OF_INTEREST |
- ← [[ODS.CONNECT_ID_LINK]]
| Column Name |
|---|
| USER_ID |
| RANK_CONNECTION |
| ACTIVE_FLAG |
| CUSTOMER_ID |
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |

