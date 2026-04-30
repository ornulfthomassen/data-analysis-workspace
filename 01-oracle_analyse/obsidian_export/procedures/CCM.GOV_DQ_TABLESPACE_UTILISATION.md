# GOV_DQ_TABLESPACE_UTILISATION

**Schema:** `CCM` | **Type:** `Procedure`

## Description
The procedure collects detailed information about Oracle tablespaces (data files and temporary files), calculates their usage and free space percentages, stores this information in a transient table (CLM_CCM.CLM_TABLESPACE), and then uses this data to insert daily data quality metrics and alerts (OK, WARNING, ERROR) based on free space thresholds into a governance data quality mart table (CLM_CCM.GOV_DQ_MARTS). It specifically focuses on tablespaces whose names start with 'CLM%'.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |

- ← [[CCM.DBA_DATA_FILES]]
| Column Name |
|---|
| TABLESPACE_NAME |
| BYTES |
| AUTOEXTENSIBLE |
| MAXBYTES |

- ← [[CCM.DBA_LMT_FREE_SPACE]]
| Column Name |
|---|
| BLOCKS |
| TABLESPACE_ID |

- ← [[SYS.TS$]]
| Column Name |
|---|
| NAME |
| TS# |
| BLOCKSIZE |

- ← [[SYS.V_$TEMP_SPACE_HEADER]]
| Column Name |
|---|
| TABLESPACE_NAME |
| BYTES_FREE |
| BYTES_USED |
| FILE_ID |

- ← [[CCM.DBA_TEMP_FILES]]
| Column Name |
|---|
| AUTOEXTENSIBLE |
| MAXBYTES |
| BYTES |
| FILE_ID |
| TABLESPACE_NAME |

- ← [[SYS.V_$TEMP_EXTENT_POOL]]
| Column Name |
|---|
| BYTES_USED |
| FILE_ID |
| TABLESPACE_NAME |

- ← [[SYS.DBA_TABLESPACES]]
| Column Name |
|---|
| TABLESPACE_NAME |
| STATUS |
| CONTENTS |
| LOGGING |
| EXTENT_MANAGEMENT |
| ALLOCATION_TYPE |
| PLUGGED_IN |
| BLOCK_SIZE |
| SEGMENT_SPACE_MANAGEMENT |
| FORCE_LOGGING |
| BIGFILE |
| DEF_TAB_COMPRESSION |
| ENCRYPTED |
| COMPRESS_FOR |

- ← [[CLM_CCM.CLM_TABLESPACE]]
| Column Name |
|---|
| TABLESPACE_NAME |
| PCT_FREE |
| LOAD_DATE |

- ← [[CLM_CCM.GOV_DQ_MARTS]]
| Column Name |
|---|
| REASON |
| PROCESS_NM |
| STATUS_NM |
| RUNTIME |
| LAST_RESSULT |


## Target Tables (Outputs)
- → [[CLM_CCM.CLM_TABLESPACE]]
| Column Name |
|---|
| LOAD_DATE |
| TABLESPACE_NAME |
| STATUS |
| CONTENTS |
| LOGGING |
| EXTENT_MANAGEMENT |
| ALLOCATION_TYPE |
| PLUGGED_IN |
| BLOCK_SIZE |
| SEGMENT_SPACE_MANAGEMENT |
| FORCE_LOGGING |
| BIGFILE |
| DEF_TAB_COMPRESSION |
| ENCRYPTED |
| COMPRESS_FOR |
| MB_MAX |
| MB_ALLOC |
| MB_FREE |
| MB_USED |
| PCT_FREE |
| PCT_USED |

- → [[CLM_CCM.GOV_DQ_MARTS]]
| Column Name |
|---|
| RUNTIME |
| FREQ |
| SYSTEM_NM |
| PROCESS_NM |
| STATUS_NM |
| REASON |
| PRIORITY |
| START_TIME |
| END_TIME |
| PREV_OK_DTTM |
| PREV_OK_RESSULT |
| LAST_RESSULT |


