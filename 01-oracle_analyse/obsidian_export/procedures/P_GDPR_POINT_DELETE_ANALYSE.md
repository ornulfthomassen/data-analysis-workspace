# P_GDPR_POINT_DELETE_ANALYSE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure (`P_GDPR_POINT_DELETE_ANALYSE`) analyzes GDPR point-deletion requests. It identifies customers (both 'EKSKUNDE'/'existing customer' and 'IKKE KUNDE'/'non-customer' based on mapping status) eligible for point-deletion from `CCDW.CUSTOMER_MAPPING`. It performs a soft-delete on 'EKSKUNDE' entries in the main customer mapping table by updating their `KURT_ID` and `MAP_STATUS`. It then reports all eligible customers for point-deletion by calling an external procedure `CCDW.P_GDPR_POINT_DELETED`. The procedure creates a temporary backup of the `CCDW.CUSTOMER_MAPPING` table before modifications, logs its actions and status into a control table (`ADM_CUSTOMER_MAPPING_CTRL_PD`), and maintains a permanent backup (`ADM_CUSTOMER_MAPPING_BCK_PD_OK`). It also checks for and raises errors if there are overdue or a high number of unhandled deletion requests.

## Data Sources (Inputs)
- ← [[CCDW.CUSTOMER_MAPPING]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |
| MAP_STATUS |
| STATUS_DATE |
| CUSTOMER_TYPE_ID |
| CUSTOMER_STATUS_ID |
| CUSTOMER_UNIT_TYPE_ID |
| OWNER_FLG |
| USER_FLG |
| OWNER_START_DATE_ORIG |
| USER_START_DATE_ORIG |
| OWNER_START_DATE |
| USER_START_DATE |
| OWNER_END_DATE |
| USER_END_DATE |
| OWNER_NUMBER_OF_TIMES |
| USER_NUMBER_OF_TIMES |
| KURT_ID_INSERT_DATE |
| KURT_ID_UPDATE_DATE |
| KURT_ID_DELETE_DATE |
- ← [[CCDW.GDPR_POINT_DEL_ANALYSE_V]]
| Column Name |
|---|
| CUSTOMER_ID |
| DELETED_DATE |
| CUSTOMER_DATE |
| ACT_LOG_ID |
- ← [[ADM_CUSTOMER_MAPPING_CTRL_PD]]
| Column Name |
|---|
| STATUS |
| ACTION |
| PERIOD_MONTH_KEY |
| STATUS_DATE |
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
- ← [[CCDW.GDPR_POINT_DELETION]]
| Column Name |
|---|
| ACT_LOG_ID |
| CUSTOMER_ID |
| REQUEST_REGISTERED_DATE |
| DELETED_ANALYSE_DATE |
| VALUE_CHAIN_MOBILE |
| ACTIVE_IN_FKM |
| VALUE_CHAIN_FIXED |
| ACTIVE_IN_DEFAKTO |
| VALUE_CHAIN_CDK |
| ACTIVE_IN_KAS |
- ← [[ODS.AGREEMENT_ODS_MOB]]
| Column Name |
|---|
| CUSTOMER_ID_OWNER |
| PRODUCT_OFFER_ID |
| END_DATE |
| SRC_AGRM_AGREEMENT_OFFER_ID |
- ← [[PD]]
| Column Name |
|---|
| PRODUCT_KEY |
| POID |
| PRODUCT_CATEGORY |
| PRODUCT_NAME |
- ← [[ODS.AGREEMENT_OFFER_ODS_MOB]]
| Column Name |
|---|
| SRC_AGRM_AGREEMENT_OFFER_ID |
| END_DATE |
| ORIGINAL_START_DATE |
| PRODUCT_OFFER_ID |
- ← [[ODS.SUBSCRIPTION_ODS_FIXED]]
| Column Name |
|---|
| CUSTOMER_ID |
| PRODUCT_OFFER_ID |
| SUBSCRIPTION_ID |
| SUBSCR_START_DATE |
| SUBSCR_END_DATE |
| CUSTOMER_ROLE_ID |
- ← [[ODS.SUBSCRIPTION_ODS_FTV]]
| Column Name |
|---|
| CUSTOMER_ID |
| PRODUCT_OFFER_ID |
| SUBSCRIPTION_ID |
| SUBSCR_START_DATE |
| SUBSCR_END_DATE |
| CUSTOMER_ROLE_ID |
- ← [[ODS.SUBSCRIPTION_ODS_MOB]]
| Column Name |
|---|
| CUSTOMER_ID |
| PRODUCT_OFFER_ID |
| SUBSCRIPTION_ID |
| SUBSCR_START_DATE |
| SUBSCR_END_DATE |
| CUSTOMER_ROLE_ID |

## Target Tables (Outputs)
- → [[CCDW.CUSTOMER_MAPPING]]
| Column Name |
|---|
| KURT_ID |
| MAP_STATUS |
- → [[ADM_CUSTOMER_MAPPING_CTRL_PD]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| STATUS_DATE |
| ACTION |
| ANTALL |
| STATUS |
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_BACKUP_PD]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |
| CUSTOMER_TYPE_ID |
| CUSTOMER_STATUS_ID |
| CUSTOMER_UNIT_TYPE_ID |
| MAP_STATUS |
| STATUS_DATE |
| OWNER_FLG |
| USER_FLG |
| OWNER_START_DATE_ORIG |
| USER_START_DATE_ORIG |
| OWNER_START_DATE |
| USER_START_DATE |
| OWNER_END_DATE |
| USER_END_DATE |
| OWNER_NUMBER_OF_TIMES |
| USER_NUMBER_OF_TIMES |
| KURT_ID_INSERT_DATE |
| KURT_ID_UPDATE_DATE |
| KURT_ID_DELETE_DATE |
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_BCK_PD_OK]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |
| CUSTOMER_TYPE_ID |
| CUSTOMER_STATUS_ID |
| CUSTOMER_UNIT_TYPE_ID |
| MAP_STATUS |
| STATUS_DATE |
| OWNER_FLG |
| USER_FLG |
| OWNER_START_DATE_ORIG |
| USER_START_DATE_ORIG |
| OWNER_START_DATE |
| USER_START_DATE |
| OWNER_END_DATE |
| USER_END_DATE |
| OWNER_NUMBER_OF_TIMES |
| USER_NUMBER_OF_TIMES |
| KURT_ID_INSERT_DATE |
| KURT_ID_UPDATE_DATE |
| KURT_ID_DELETE_DATE |
- → [[CRM_ANALYSE.ADM_LOAD_HISTORY]]
| Column Name |
|---|
| TABLE_NAME |
| RUN_DATE |
| STATUS |
| MESSAGE |
- → [[CCDW.GDPR_POINT_DELETION]]
| Column Name |
|---|
| DELETED_ANALYSE_DATE |

