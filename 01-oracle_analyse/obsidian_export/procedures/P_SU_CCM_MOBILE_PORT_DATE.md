# P_SU_CCM_MOBILE_PORT_DATE

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This procedure refreshes the 'CCM_MOBILE_PORT_DATES' table with current mobile porting order data. It achieves this by first populating a temporary staging table ('CCM_MOBILE_PORT_DATES_TMP') with aggregated and transformed information from various online reporting (ONL_REP) and data warehouse (CCDW) source tables. After successful population, it performs a 'table swap' where the existing 'CCM_MOBILE_PORT_DATES' table is renamed to a backup table ('CCM_MOBILE_PORT_DATES_BK'), and the newly populated temporary table is renamed to 'CCM_MOBILE_PORT_DATES'. It also manages indexes and grants permissions during this process. Errors are logged to 'CLM_CCM.CCM_LOAD_HISTORY'.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_MOBILE_PORT_DATES]]
- ← [[ONL_REP.SERVICE_ORDER]]
| Column Name |
|---|
| ORDER_ID |
| ORDER_ARRIVAL_DATE |
| ORDER_STATUS_ID |
| ORDER_PROCESSED_DATE |
| ORDER_ACTION_TYPE_ID |
- ← [[ONL_REP.SERVICE_ORDER_CUSTOMER]]
| Column Name |
|---|
| ORDER_ID |
| CUST_ROLE_ID |
| CUST_ID |
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
| Column Name |
|---|
| ORDER_ID |
| PRODUCT_ACTION_TYPE_ID |
| ORDER_PHONE_NUM |
| SUBSCR_ID |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |
| SUBSCRIPTION_ID |
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT_PARAM]]
| Column Name |
|---|
| ORDER_ID |
| ORDER_LINE_ID |
| PARAM_ID |
| PARAM_VALUE |
| PARAM_STATUS_ID |

## Target Tables (Outputs)
- → [[CLM_CCM.CCM_MOBILE_PORT_DATES_TMP]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| PORT_ORDER_ID |
| PORT_ORDER_DATE |
| PORT_DATE |
| DAYS_UNTIL_PORT |
| SERVICE_PROVIDER_NAME |
| ORDER_STATUS |
| INFO_CHG_DATE |
| SECOND_WB_PORT_FLG |
| CU_NO_PORT_SUBSCRIPTIONS |
| OWNER_KURT_ID |
| SRC_SUBSCRIPTION_ID |
- → [[CLM_CCM.CCM_MOBILE_PORT_DATES_BK]]
- → [[CLM_CCM.CCM_MOBILE_PORT_DATES]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| PORT_ORDER_ID |
| PORT_ORDER_DATE |
| PORT_DATE |
| DAYS_UNTIL_PORT |
| SERVICE_PROVIDER_NAME |
| ORDER_STATUS |
| INFO_CHG_DATE |
| SECOND_WB_PORT_FLG |
| CU_NO_PORT_SUBSCRIPTIONS |
| OWNER_KURT_ID |
| SRC_SUBSCRIPTION_ID |
- → [[CLM_CCM.CCM_LOAD_HISTORY]]
| Column Name |
|---|
| TABLE_NAME |
| LOAD_START_DTTM |
| LOAD_STATUS |
| STATUS_MESSAGE |
| POWERCENTER_WF_NAME |
| POWERCENTER_S_NAME |

