# ADM17_PORT_HISTORY

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Manages and populates historical mobile number porting data into a partitioned table, CRM_ANALYSE.ADM_PORT_HISTORY, by aggregating information from NRPORT.NRPORT_PORTERINGER and validating against GALAXY.DATE_DIM_MV and CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY for specified monthly periods. It handles table and partition creation if they do not exist.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
| SUBOBJECT_NAME |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
- ← [[NRPORT.NRPORT_PORTERINGER]]
| Column Name |
|---|
| PORT_LOG_VALID_FROM_DATE |
| MSISDN_ID |
| SERVICE_PROVIDER_ID_PORT_FROM |
| SERVICE_PROVIDER_ID_PORT_TO |
- ← [[CRM_ANALYSE.ADM_PORT_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_PORT_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| MAIN_NUMBER |
| ANT_TELENOR |
| ANTALL |
| SHOPPER_FLG |
| FIRST_PORT_DATE |
| LAST_PORT_DATE |
| FIRST_PORT_IN_SERV_PROV_ID |
| FIRST_PORT_IN_SERV_PROV_NAME |
| LAST_PORT_IN_SERV_PROV_ID |
| LAST_PORT_IN_SERV_PROV_NAME |
| FIRST_PORT_OUT_SERV_PROV_ID |
| FIRST_PORT_OUT_SERV_PROV_NAME |
| LAST_PORT_OUT_SERV_PROV_ID |
| LAST_PORT_OUT_SERV_PROV_NAME |

