# P_EV_ODS_EVENT_SUB_ACTIVATION_MOB

**Schema:** `CCM` | **Type:** `Procedure`

## Description
The procedure performs a full reload of the `ODS_EVENT_SUB_ACTIVATION_MOB` table. It identifies activated subscriptions by extracting and processing order-related data from `ODS_EVENT_ORDER_ONL_MOB` and handset usage information from `HANDSET_LAST_USED_V`. The processed data is first loaded into a temporary work table (`WORK_ACTIVATION_LOOKUP_MOB`), then into a new staging table (`ODS_EVENT_SUB_ACTIVATION_MOB_N`). After validating the row count against the existing target table, it performs a table swap: the old `ODS_EVENT_SUB_ACTIVATION_MOB` is renamed to a backup table (`_O`), and the new staging table (`_N`) is renamed to become the new `ODS_EVENT_SUB_ACTIVATION_MOB`. Intermediate work tables and the old backup table are subsequently dropped.

## Data Sources (Inputs)
- ← [[CLM_CCM.ODS_EVENT_SUB_ACTIVATION_MOB]]
- ← [[CLM_CCM.ODS_EVENT_ORDER_ONL_MOB]]
| Column Name |
|---|
| SRC_ORDER_ID |
| ORDER_PHONENUMBER |
| SRC_SUBSCR_ID |
| ORDER_PROCESSED_DATE |
| ORDER_ACTION_TYPE_ID |
| PRODUCT_ACTION_TYPE_ID |
| OWNERSHIP_TRANSFERE_TYPE |
| ORDER_STATUS_ID |
| SOURCE_SYSTEM_KEY |

- ← [[CCDW.HANDSET_LAST_USED_V]]
| Column Name |
|---|
| IMEI_LAST_USED_DT_KEY |
| TERMINAL_USE_LAST_DATE |
| SUBSCRIPTION_ID |
| IMEI |
| SUB_NUMBER |


## Target Tables (Outputs)
- → [[CLM_CCM.WORK_ACTIVATION_LOOKUP_MOB]]
| Column Name |
|---|
| SRC_ORDER_ID |
| ORDER_PHONENUMBER |
| SRC_SUBSCR_ID |
| ORDER_PROCESSED_DATE |
| ORDER_ACTION_TYPE_ID |
| PRODUCT_ACTION_TYPE_ID |
| OWNERSHIP_TRANSFERE_TYPE |
| R_NUM |

- → [[CLM_CCM.ODS_EVENT_SUB_ACTIVATION_MOB_N]]
| Column Name |
|---|
| EVENT_DATE_ID |
| EVENT_DATE |
| MAIN_NUMBER |
| SUBSCRIPTION_ID |
| IMEI_USE |
| LOAD_DATE |

- → [[CLM_CCM.ODS_EVENT_SUB_ACTIVATION_MOB]]
| Column Name |
|---|
| EVENT_DATE_ID |
| EVENT_DATE |
| MAIN_NUMBER |
| SUBSCRIPTION_ID |
| IMEI_USE |
| LOAD_DATE |


