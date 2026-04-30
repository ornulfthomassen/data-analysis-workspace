# P_CU_ODS_CUSTOMER_ADDRESS

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Refreshes the ODS_CUSTOMER_ADDRESS table with transformed customer address data derived from various customer and subscription-related source tables. It employs a common zero-downtime table swap strategy, where data is first loaded into a temporary table, then the temporary table is renamed to become the new main table, and the old main table is moved to a backup. The procedure includes checks for data volume changes to prevent erroneous swaps and logs operational status and errors.

## Data Sources (Inputs)
- ← [[CLM_CCM.ODS_FAR_GROUP]]
| Column Name |
|---|
| FARID |
| ADDRESS_STATUS |
| BOLIG_FAR_1 |
| GAB_FLAT |
| GAB_NUMBER |

- ← [[CLM_CCM.CCM_SUBSCRIPTION_V]]
| Column Name |
|---|
| OWNER_KURT_ID |
| INSTALLATION_FARID |
| MAIN_PRODUCT_ID |
| USER_KURT_ID |

- ← [[ODS.CUSTOMER_ODS]]
| Column Name |
|---|
| CUSTOMER_ID |
| CUSTOMER_STATUS_ID |
| CUSTOMER_TYPE_ID |

- ← [[CCDW.HOUSEHOLD_MEMBER]]
| Column Name |
|---|
| GEOGRAPHY_ID |
| CUSTOMER_ID |

- ← [[CCDW.CUSTOMER]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_UNIT_TYPE_ID |


## Target Tables (Outputs)
- → [[CCM.ODS_CUSTOMER_ADDRESS]]
| Column Name |
|---|
| KURT_ID |
| FARID |
| ADD_TYPE |
| GAB_FLAT |
| GAB_NUMBER |
| KURT_ID_CHAR |
| KURT_TYPE |
| LOAD_DTTM |

- → [[CCM.ODS_CUSTOMER_ADDRESS_N]]
| Column Name |
|---|
| KURT_ID |
| FARID |
| ADD_TYPE |
| GAB_FLAT |
| GAB_NUMBER |
| KURT_ID_CHAR |
| KURT_TYPE |
| LOAD_DTTM |

- → [[CCM.ODS_CUSTOMER_ADDRESS_O]]
| Column Name |
|---|
| KURT_ID |
| FARID |
| ADD_TYPE |
| GAB_FLAT |
| GAB_NUMBER |
| KURT_ID_CHAR |
| KURT_TYPE |
| LOAD_DTTM |

- → [[CCM.ODS_CUSTOMER_ADDRESS_O_TEM]]
| Column Name |
|---|
| KURT_ID |
| FARID |
| ADD_TYPE |
| GAB_FLAT |
| GAB_NUMBER |
| KURT_ID_CHAR |
| KURT_TYPE |
| LOAD_DTTM |

- → [[CLM_CCM.ODS_PROCEDURE_SWAP_STATUS]]
| Column Name |
|---|
| PROC_NAME |
| LOG_DTTM |
| STATUS_MESSAGE |
| MAIN_TABLE_ROW_COUNT |
| TEMP_TABLE_ROW_COUNT |

- → [[CLM_CCM.CCM_LOAD_HISTORY]]
| Column Name |
|---|
| OBJECT_NAME |
| START_DTTM |
| STATUS |
| MESSAGE |
| POWERCENTER_WF_NAME |
| POWERCENTER_S_NAME |


