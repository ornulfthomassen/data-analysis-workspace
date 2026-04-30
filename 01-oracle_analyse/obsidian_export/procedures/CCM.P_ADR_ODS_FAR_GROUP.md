# P_ADR_ODS_FAR_GROUP

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Refreshes the ODS_FAR_GROUP table with aggregated address data from CLM_CCM.ODS_FAR using a controlled table-swap mechanism. It first populates a new temporary table, then conditionally renames the existing ODS_FAR_GROUP to a backup table (ODS_FAR_GROUP_O) and the temporary table to ODS_FAR_GROUP. This process ensures data consistency, provides a rollback mechanism, and logs execution status and potential issues.

## Data Sources (Inputs)
- ← [[CLM_CCM.ODS_FAR]]
| Column Name |
|---|
| FARID |
| ADDRESS_STATUS |
| ADDRESS_TYPE |
| FLATNUMBER |
| GAB_NUMBER |
| STREETPOSTALCODE |
| STREETNAME |

- ← [[CCM.ALL_TABLES]]
| Column Name |
|---|
| owner |
| table_name |
| num_rows |

- ← [[CCM.ALL_INDEXES]]
| Column Name |
|---|
| owner |
| table_name |
| index_name |

- ← [[CCM.USER_INDEXES]]
| Column Name |
|---|
| index_name |
| table_name |
| table_owner |
| generated |

- ← [[CCM.DUAL]]

## Target Tables (Outputs)
- → [[CCM.ODS_FAR_GROUP_N]]
| Column Name |
|---|
| FARID |
| FLATNUMBER |
| GAB_NUMBER |
| GAB_FLAT |
| BOLIG_FAR_1 |
| BOLIG_FAR_2 |
| ADDRESS_TYPE |
| ADDRESS_STATUS |
| STREETPOSTALCODE |
| LOADED_DTTM |

- → [[CCM.ODS_FAR_GROUP]]
| Column Name |
|---|
| FARID |
| FLATNUMBER |
| GAB_NUMBER |
| GAB_FLAT |
| BOLIG_FAR_1 |
| BOLIG_FAR_2 |
| ADDRESS_TYPE |
| ADDRESS_STATUS |
| STREETPOSTALCODE |
| LOADED_DTTM |

- → [[CCM.ODS_FAR_GROUP_O]]
| Column Name |
|---|
| FARID |
| FLATNUMBER |
| GAB_NUMBER |
| GAB_FLAT |
| BOLIG_FAR_1 |
| BOLIG_FAR_2 |
| ADDRESS_TYPE |
| ADDRESS_STATUS |
| STREETPOSTALCODE |
| LOADED_DTTM |

- → [[CCM.ODS_FAR_GROUP_O_TEMP]]
| Column Name |
|---|
| FARID |
| FLATNUMBER |
| GAB_NUMBER |
| GAB_FLAT |
| BOLIG_FAR_1 |
| BOLIG_FAR_2 |
| ADDRESS_TYPE |
| ADDRESS_STATUS |
| STREETPOSTALCODE |
| LOADED_DTTM |

- → [[CLM_CCM.ODS_PROCEDURE_SWAP_STATUS]]
| Column Name |
|---|
| PROC_NAME |
| DTTM |
| MESSAGE |
| OLD_ROW_COUNT |
| NEW_ROW_COUNT |

- → [[CLM_CCM.CCM_LOAD_HISTORY]]
| Column Name |
|---|
| TABLE_NAME |
| START_DTTM |
| STATUS |
| MESSAGE |
| POWERCENTER_WF_NAME |
| POWERCENTER_S_NAME |


