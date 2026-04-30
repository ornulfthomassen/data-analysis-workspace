# P_EV_ODS_EVENT_ORDER_ONL_MOB

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Loads and aggregates data related to activated mobile subscriptions, performing a full load into a target table (`ODS_EVENT_SUB_ACTIVATION_MOB`) using a swap mechanism for data freshness and reliability. It identifies active subscriptions based on order and traffic data, storing activation event details for personalization and onboarding.

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

- ← [[CCDW_USAGE.TRAFFIC_DAY]]
| Column Name |
|---|
| EVENT_DATE_ID |
| MAIN_NUMBER |
| SUBSCRIPTION_ID |
| IMEI |
| BUSINESS_AREA_ID |

- ← [[CLM_CCM.WORK_ACTIVATION_LOOKUP_MOB]]
| Column Name |
|---|
| ORDER_PHONENUMBER |
| R_NUM |


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
| R_NUM |

- → [[CLM_CCM.ODS_EVENT_SUB_ACTIVATION_MOB_O]]
- → [[CLM_CCM.ODS_EVENT_SUB_ACTIVATION_MOB]]
| Column Name |
|---|
| EVENT_DATE_ID |
| EVENT_DATE |
| MAIN_NUMBER |
| SUBSCRIPTION_ID |
| IMEI_USE |
| LOAD_DATE |
| R_NUM |

- → [[CLM_CCM.CCM_LOAD_HISTORY]]
| Column Name |
|---|
| TARGET_TABLE_NAME |
| START_TIMESTAMP |
| JOB_STATUS |
| STATUS_MESSAGE |
| POWERCENTER_WF_NAME |
| POWERCENTER_S_NAME |


