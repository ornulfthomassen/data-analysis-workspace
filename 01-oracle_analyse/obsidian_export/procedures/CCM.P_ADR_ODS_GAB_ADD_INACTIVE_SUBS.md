# P_ADR_ODS_GAB_ADD_INACTIVE_SUBS

**Schema:** `CCM` | **Type:** `Procedure`

## Description
The procedure calculates and aggregates inactive subscription product counts and their inactive dates, associating them with GAB_FLAT and GAB_NUMBER from the ODS_FAR_GROUP. It then performs a robust, controlled table-swapping operation to update a main ODS table (`ODS_GAB_ADD_INACTIVE_SUBS`) with this newly generated data. The swap mechanism includes checks for data deviation, temporary and backup table management, index creation and renaming, and comprehensive logging of status and errors.

## Data Sources (Inputs)
- ← [[CLM_CCM.ODS_FAR_GROUP]]
| Column Name |
|---|
| GAB_FLAT |
| GAB_NUMBER |
| FARID |
| ADDRESS_STATUS |

- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| END_DATE |
| BUSINESS_AREA_ID |
| PRODUCT_OFFER_ID |
| SUBSCRIPTION_ID |

- ← [[CCDW.SUBSCRIPTION_ADDRESS]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| GEOGRAPHY_ID_USER |

- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| DRM_COMMON_TECHNOLOGY |
| DRM_COMMON_REPORTING |

- ← [[CCM.ALL_TABLES]]
| Column Name |
|---|
| OWNER |
| TABLE_NAME |
| NUM_ROWS |

- ← [[CCM.ALL_INDEXES]]
| Column Name |
|---|
| OWNER |
| TABLE_NAME |
| INDEX_NAME |

- ← [[CCM.USER_INDEXES]]
| Column Name |
|---|
| INDEX_NAME |
| TABLE_NAME |
| TABLE_OWNER |
| GENERATED |


## Target Tables (Outputs)
- → [[CCM.ODS_GAB_ADD_INACTIVE_SUBS]]
| Column Name |
|---|
| LOAD_DTTM |
| GAB_FLAT |
| GAB_NUMBER |
| NO_INA_GABF_DSL |
| NO_INA_GABF_TBB |
| NO_INA_GABF_COAX |
| NO_INA_GABF_C_FTTH |
| NO_INA_GABF_L_FTTH |
| NO_INA_GABF_TV |
| INA_DT_GABF_DSL |
| INA_DT_GABF_TBB |
| INA_DT_GABF_COAX |
| INA_DT_GABF_C_FTTH |
| INA_DT_GABF_L_FTTH |
| INA_DT_GABF_TV |
| NO_INA_DSL |
| NO_INA_TBB |
| NO_INA_COAX |
| NO_INA_C_FTTH |
| NO_INA_L_FTTH |
| NO_INA_TV |
| INA_DT_DSL |
| INA_DT_TBB |
| INA_DT_COAX |
| INA_DT_CDK_FTTH |
| INA_DT_LUM_FTTH |
| INA_DT_TV |

- → [[CCM.ODS_GAB_ADD_INACTIVE_SUBS_N]]
| Column Name |
|---|
| LOAD_DTTM |
| GAB_FLAT |
| GAB_NUMBER |
| NO_INA_GABF_DSL |
| NO_INA_GABF_TBB |
| NO_INA_GABF_COAX |
| NO_INA_GABF_C_FTTH |
| NO_INA_GABF_L_FTTH |
| NO_INA_GABF_TV |
| INA_DT_GABF_DSL |
| INA_DT_GABF_TBB |
| INA_DT_GABF_COAX |
| INA_DT_GABF_C_FTTH |
| INA_DT_GABF_L_FTTH |
| INA_DT_GABF_TV |
| NO_INA_DSL |
| NO_INA_TBB |
| NO_INA_COAX |
| NO_INA_C_FTTH |
| NO_INA_L_FTTH |
| NO_INA_TV |
| INA_DT_DSL |
| INA_DT_TBB |
| INA_DT_COAX |
| INA_DT_CDK_FTTH |
| INA_DT_LUM_FTTH |
| INA_DT_TV |

- → [[CCM.ODS_GAB_ADD_INACTIVE_SUBS_O]]
| Column Name |
|---|
| LOAD_DTTM |
| GAB_FLAT |
| GAB_NUMBER |
| NO_INA_GABF_DSL |
| NO_INA_GABF_TBB |
| NO_INA_GABF_COAX |
| NO_INA_GABF_C_FTTH |
| NO_INA_GABF_L_FTTH |
| NO_INA_GABF_TV |
| INA_DT_GABF_DSL |
| INA_DT_GABF_TBB |
| INA_DT_GABF_COAX |
| INA_DT_GABF_C_FTTH |
| INA_DT_GABF_L_FTTH |
| INA_DT_GABF_TV |
| NO_INA_DSL |
| NO_INA_TBB |
| NO_INA_COAX |
| NO_INA_C_FTTH |
| NO_INA_L_FTTH |
| NO_INA_TV |
| INA_DT_DSL |
| INA_DT_TBB |
| INA_DT_COAX |
| INA_DT_CDK_FTTH |
| INA_DT_LUM_FTTH |
| INA_DT_TV |

- → [[CCM.ODS_GAB_ADD_INACTIVE_SUBS_TEMP]]
| Column Name |
|---|
| LOAD_DTTM |
| GAB_FLAT |
| GAB_NUMBER |
| NO_INA_GABF_DSL |
| NO_INA_GABF_TBB |
| NO_INA_GABF_COAX |
| NO_INA_GABF_C_FTTH |
| NO_INA_GABF_L_FTTH |
| NO_INA_GABF_TV |
| INA_DT_GABF_DSL |
| INA_DT_GABF_TBB |
| INA_DT_GABF_COAX |
| INA_DT_GABF_C_FTTH |
| INA_DT_GABF_L_FTTH |
| INA_DT_GABF_TV |
| NO_INA_DSL |
| NO_INA_TBB |
| NO_INA_COAX |
| NO_INA_C_FTTH |
| NO_INA_L_FTTH |
| NO_INA_TV |
| INA_DT_DSL |
| INA_DT_TBB |
| INA_DT_COAX |
| INA_DT_CDK_FTTH |
| INA_DT_LUM_FTTH |
| INA_DT_TV |

- → [[CLM_CCM.ODS_PROCEDURE_SWAP_STATUS]]
| Column Name |
|---|
| PROCEDURE_NAME |
| LOG_DTTM |
| MESSAGE |
| PREV_ROW_COUNT |
| NEW_ROW_COUNT |

- → [[CLM_CCM.CCM_LOAD_HISTORY]]
| Column Name |
|---|
| TABLE_NAME |
| START_DATETIME |
| STATUS |
| ERROR_MESSAGE |
| POWERCENTER_WF_NAME |
| POWERCENTER_S_NAME |


