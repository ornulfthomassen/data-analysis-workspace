# P_SU_CCM_SUBSCRIPTION_EVENTS

**Schema:** `CCM` | **Type:** `Procedure`

## Description
The procedure extracts recent invoice-related data from source views, processes and aggregates it, and then loads this transformed data into a new staging table. It performs a 'table swap' where the current permanent target table is renamed as a backup, and the new staging table is renamed to become the active permanent target table. This ensures atomic updates and provides a backup. The process includes checks for data volume changes, index creation, privilege granting, and comprehensive logging of its execution status.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_SUBSCRIPTION_EVENTS]]
- ← [[GALAXY.INVOICE_DETAIL_FACT_V]]
| Column Name |
|---|
| PAYER_CUSTOMER_KEY |
| PAYER_ACCOUNT_KEY |
| SUBSCRIPTION_KEY |
| INVOICE_ID |
| INVOICE_DT_KEY |
| INVOICE_LINE_TYPE_KEY |
| TRAFFIC_DATAVOLUME |
| INVOICE_GROSS_AMOUNT |
| SOURCE_SYSTEM_KEY |
| MARKET_AREA_KEY |
- ← [[GALAXY.INVOICE_LINE_TYPE_DIM_V]]
| Column Name |
|---|
| INVOICE_LINE_TYPE_KEY |
| INVOICE_LINE_TYPE_DESC |
| INVOICE_LINE_TYPE_NAME |
- ← [[ALL_INDEXES]]
| Column Name |
|---|
| OWNER |
| TABLE_NAME |
| INDEX_NAME |

## Target Tables (Outputs)
- → [[CLM_CCM.WORK_EVENT_30_INVOICE]]
| Column Name |
|---|
| KURT_ID |
| SUBSCRIPTION_ID |
| EVENT_ID |
| EVENT_NM |
| EVENT_DETAIL |
| EVENT_DTTM |
| EVENT_DETECTION_DTTM |
| EVENT_VALID_TO_DTTM |
| MAIN_NUMBER |
| EVENT_VALUE_1_DESC |
| EVENT_VALUE_1 |
| EVENT_VALUE_2_DESC |
| EVENT_VALUE_2 |
| EVENT_VALUE_NUM_1_DESC |
| EVENT_VALUE_NUM_1 |
| R_NUM |
- → [[CLM_CCM.CCM_SUBSCRIPTION_EVENTS_N]]
| Column Name |
|---|
| KURT_ID |
| SUBSCRIPTION_ID |
| EVENT_ID |
| EVENT_NM |
| EVENT_DETAIL |
| EVENT_DTTM |
| EVENT_DETECTION_DTTM |
| EVENT_VALID_TO_DTTM |
| MAIN_NUMBER |
| EVENT_VALUE_1_DESC |
| EVENT_VALUE_1 |
| EVENT_VALUE_2_DESC |
| EVENT_VALUE_2 |
| EVENT_VALUE_3_DESC |
| EVENT_VALUE_3 |
| EVENT_VALUE_4_DESC |
| EVENT_VALUE_4 |
| EVENT_VALUE_NUM_1_DESC |
| EVENT_VALUE_NUM_1 |
| EVENT_VALUE_NUM_2_DESC |
| EVENT_VALUE_NUM_2 |
| EVENT_VALUE_NUM_3_DESC |
| EVENT_VALUE_NUM_3 |
| EVENT_VALUE_NUM_4_DESC |
| EVENT_VALUE_NUM_4 |
| EVENT_VALUE_NUM_5_DESC |
| EVENT_VALUE_NUM_5 |
| EVENT_VALUE_NUM_6_DESC |
| EVENT_VALUE_NUM_6 |
- → [[CLM_CCM.CCM_SUBSCRIPTION_EVENTS_O]]
- → [[CLM_CCM.CCM_SUBSCRIPTION_EVENTS]]
- → [[CLM_CCM.CCM_LOAD_HISTORY]]
| Column Name |
|---|
| TABLE_NAME |
| START_TIME |
| STATUS |
| STATUS_MESSAGE |
| WORKFLOW_NAME |
| SESSION_NAME |

