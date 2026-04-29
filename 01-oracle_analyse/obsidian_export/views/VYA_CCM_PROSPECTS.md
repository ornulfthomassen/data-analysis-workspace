# VYA_CCM_PROSPECTS

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies consumer prospects, primarily mobile, who are not currently undergoing a port-in process with specific telecom operators (Telenor, Talkmore, Dipper), providing key performance indicator (KPI) flags and contact details for forecasting in a system like Viya. It filters out prospects whose associated phone numbers are linked to recent service orders involving port-ins from these operators.

## Data Sources (Inputs)
- ← [[ONL_REP.SERVICE_ORDER]]
| Column Name |
|---|
| ORDER_ID |
| ORDER_STATUS_ID |
| ORDER_ORIGINATOR_ID |
| ORDER_PROCESSED_DATE |
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
| Column Name |
|---|
| ORDER_ID |
| ORDER_PHONE_NUM |
| PRODUCT_ACTION_TYPE_ID |
| PRODUCT_STATUS_ID |
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT_PARAM]]
| Column Name |
|---|
| ORDER_ID |
| PARAM_ID |
| PARAM_VALUE |
- ← [[CLM_CCM.ODS_LEADS_CONSUMER]]
| Column Name |
|---|
| LEADS_SUBJECT_KEY |
| LEADS_SUBJECT_TYPE |
| NBR_LEAD_RESOURCES |
| LOAD_DTTM |
| LEAD_RESOURCE_1 |
| LEAD_RESOURCE_2 |
| LEAD_RESOURCE_3 |
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
| Column Name |
|---|
| CUSTOMER_KEY |
| KURT_ID |

