# P_ADM_MOBIL_PORT_HISTORY

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Generates and loads mobile number portability history for a specified month into a partitioned data warehouse table. It aggregates mobile number porting events and related subscription data, performs source data validation, and manages table partitions by creating or overwriting monthly partitions.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
- ← [[NRPORT.NRPORT_PORTERINGER]]
| Column Name |
|---|
| MSISDN_ID |
| PORT_LOG_VALID_FROM_DATE |
| SERVICE_PROVIDER_ID_PORT_FROM |
| SERVICE_PROVIDER_ID_PORT_TO |
- ← [[ADM_MOB_SUBSCRIPTION_CORE]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| END_DATE |

## Target Tables (Outputs)
- → [[TMP_MOBIL_PORT_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
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
- → [[ADM_MOBIL_PORT_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
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

