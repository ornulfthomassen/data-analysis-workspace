# P_CU_ODS_CUSTOMER_COMM_FREEZE

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Refreshes the ODS_CUSTOMER_COMM_FREEZE table using a table swap mechanism. It first constructs new customer communication freeze data by combining information from CM.CUSTOMER, CCDW.GDPR_POINT_DELETION, and CCDW_SEGMENT.COMMUNICATION_FREEZE into a temporary table. After validating row count changes within a specified threshold, it renames the current ODS_CUSTOMER_COMM_FREEZE table to a backup table (ODS_CUSTOMER_COMM_FREEZE_O) and promotes the temporary table to become the new ODS_CUSTOMER_COMM_FREEZE. The procedure also handles initial loads, index management, and logs its activities and any exceptions to CLM_CCM.ODS_PROCEDURE_SWAP_STATUS.

## Data Sources (Inputs)
- ← [[CM.CUSTOMER]]
| Column Name |
|---|
| CUST_ID |
| KURT_ID |
| MASTER_ID |
| INFO_REG_DATE |
| INFO_IS_DELETED |
| CUST_UNIT_NUMBER |
| ADDR_CO_NAME |

- ← [[CCDW.GDPR_POINT_DELETION]]
| Column Name |
|---|
| CUSTOMER_ID |
| REQUEST_REGISTERED_DATE |
| ACT_LOG_ID |

- ← [[CCDW_SEGMENT.COMMUNICATION_FREEZE]]
| Column Name |
|---|
| KURT_ID |
| REASON |
| START_DATE |
| END_DATE |
| COMMUNICATION_FREEZE_ID |


## Target Tables (Outputs)
- → [[CCM.ODS_CUSTOMER_COMM_FREEZE]]
| Column Name |
|---|
| KURT_ID |
| MASTER_ID |
| VALID_FROM_DATE |
| VALID_TO_DATE |
| BL_MOBILE_FLAG |
| BL_FIXED_FLAG |
| REASON |
| COMMUNICATION_FREEZE_ID |
| REASON_PROIRITY |
| LOAD_DTTM |

- → [[CCM.ODS_CUSTOMER_COMM_FREEZE_N]]
| Column Name |
|---|
| KURT_ID |
| MASTER_ID |
| VALID_FROM_DATE |
| VALID_TO_DATE |
| BL_MOBILE_FLAG |
| BL_FIXED_FLAG |
| REASON |
| COMMUNICATION_FREEZE_ID |
| REASON_PROIRITY |
| LOAD_DTTM |

- → [[CCM.ODS_CUSTOMER_COMM_FREEZE_O]]
| Column Name |
|---|
| KURT_ID |
| MASTER_ID |
| VALID_FROM_DATE |
| VALID_TO_DATE |
| BL_MOBILE_FLAG |
| BL_FIXED_FLAG |
| REASON |
| COMMUNICATION_FREEZE_ID |
| REASON_PROIRITY |
| LOAD_DTTM |

- → [[CCM.ODS_CUSTOMER_COMM_FREEZE_O_TEM]]
| Column Name |
|---|
| KURT_ID |
| MASTER_ID |
| VALID_FROM_DATE |
| VALID_TO_DATE |
| BL_MOBILE_FLAG |
| BL_FIXED_FLAG |
| REASON |
| COMMUNICATION_FREEZE_ID |
| REASON_PROIRITY |
| LOAD_DTTM |

- → [[CLM_CCM.ODS_PROCEDURE_SWAP_STATUS]]
| Column Name |
|---|
| PROC_NAME |
| LOG_DATE |
| STATUS_MESSAGE |
| MAIN_TABLE_ROW_COUNT |
| TEMP_TABLE_ROW_COUNT |


