# ADM_MPORT

**Schema:** `CCM` | **Type:** `View`

## Description
Combines porting order details with subscription mapping information to identify a relevant 'MAIN_ID_SK' for each porting record. It enriches the porting data by matching on phone numbers and date ranges, also deriving a 'PORT_PERIOD' from the port date.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.MPORT_PORT_REPORT]]
| Column Name |
|---|
| ORDER_ARRIVAL_DATE |
| ORDER_ID |
| PORT_DATE |
| SERVICE_PROVIDER_ID_OUT |
| SERVICE_PROVIDER_ID_OUT_NAME |
| ORDER_STATUS_ID |
| INFO_CHG_DATE |
| FETCHED_DATE |
| ORDER_PHONE_NUM |

- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| main_id_sk |
| main_number_rank |
| main_number |
| start_date |
| end_date |


