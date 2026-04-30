# P_ADR_ODS_GAB_ADD_INSTALL_SUBS

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Refreshes and manages the 'ODS_GAB_ADD_INSTALL_SUBS' table using a table swap strategy. It populates a new temporary table with aggregated product and address data from various source systems, then conditionally renames this temporary table to become the new main table. The old main table is either archived as a backup, temporarily renamed and dropped, or created if it doesn't exist, based on row count comparisons and existence checks. The procedure also handles index creation/renaming for the involved tables and logs its operational status and any encountered errors or warnings.

## Data Sources (Inputs)
- ← [[CLM_CCM.ODS_FAR_GROUP]]
| Column Name |
|---|
| GAB_FLAT |
| GAB_NUMBER |
| FARID |
| ADDRESS_STATUS |

- ← [[CLM_CCM.CCM_SUBSCRIPTION_V]]
| Column Name |
|---|
| INSTALLATION_FARID |
| MAIN_PRODUCT_ID |

- ← [[CLM_CCM.ODS_PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| DRM_COMMON_TECHNOLOGY |
| PRODUCT_NAME |
| SOURCE_SYSTEM_NAME |

- ← [[CLM_FIXED_CCM.FTV_CCM_ADDRESS_SEGMENT_V]]
| Column Name |
|---|
| ADR_ID |
| ADR_SEGMENT |
| ADR_TYPE_DETAIL2 |

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
| INDEX_NAME |
| TABLE_NAME |
| TABLE_OWNER |
| GENERATED |

- ← [[CCM.DUAL]]

## Target Tables (Outputs)
- → [[CCM.ODS_GAB_ADD_INSTALL_SUBS]]
| Column Name |
|---|
| LOAD_DTTM |
| GAB_FLAT |
| GAB_NUMBER |
| ADR_SEGMENT |
| ADR_TYPE_DETAIL2 |
| FTV_PRODUCT_DSL |
| FTV_PRODUCT_TBB |
| FTV_PRODUCT_COAX |
| FTV_PRODUCT_CDK_FTTH |
| FTV_PRODUCT_LUM_FTTH |
| FTV_PRODUCT_TV |
| NO_DSL |
| NO_TBB |
| NO_COAX |
| NO_CDK_FTTH |
| NO_LUM_FTTH |
| NO_TV |
| FTV_PRODUCT_DSL_GABFLAT |
| FTV_PRODUCT_TBB_GABFLAT |
| FTV_PRODUCT_COAX_GABFLAT |
| FTV_PRODUCT_CDK_FTTH_GABFLAT |
| FTV_PRODUCT_LUM_FTTH_GABFLAT |
| FTV_PRODUCT_TV_GABFLAT |
| NO_DSL_GABF |
| NO_TBB_GABF |
| NO_COAX_GABF |
| NO_CDK_FTTH_GABF |
| NO_LUM_FTTH_GABF |
| NO_TV_GABF |

- → [[CCM.ODS_GAB_ADD_INSTALL_SUBS_N]]
| Column Name |
|---|
| LOAD_DTTM |
| GAB_FLAT |
| GAB_NUMBER |
| ADR_SEGMENT |
| ADR_TYPE_DETAIL2 |
| FTV_PRODUCT_DSL |
| FTV_PRODUCT_TBB |
| FTV_PRODUCT_COAX |
| FTV_PRODUCT_CDK_FTTH |
| FTV_PRODUCT_LUM_FTTH |
| FTV_PRODUCT_TV |
| NO_DSL |
| NO_TBB |
| NO_COAX |
| NO_CDK_FTTH |
| NO_LUM_FTTH |
| NO_TV |
| FTV_PRODUCT_DSL_GABFLAT |
| FTV_PRODUCT_TBB_GABFLAT |
| FTV_PRODUCT_COAX_GABFLAT |
| FTV_PRODUCT_CDK_FTTH_GABFLAT |
| FTV_PRODUCT_LUM_FTTH_GABFLAT |
| FTV_PRODUCT_TV_GABFLAT |
| NO_DSL_GABF |
| NO_TBB_GABF |
| NO_COAX_GABF |
| NO_CDK_FTTH_GABF |
| NO_LUM_FTTH_GABF |
| NO_TV_GABF |

- → [[CCM.ODS_GAB_ADD_INSTALL_SUBS_O]]
| Column Name |
|---|
| LOAD_DTTM |
| GAB_FLAT |
| GAB_NUMBER |
| ADR_SEGMENT |
| ADR_TYPE_DETAIL2 |
| FTV_PRODUCT_DSL |
| FTV_PRODUCT_TBB |
| FTV_PRODUCT_COAX |
| FTV_PRODUCT_CDK_FTTH |
| FTV_PRODUCT_LUM_FTTH |
| FTV_PRODUCT_TV |
| NO_DSL |
| NO_TBB |
| NO_COAX |
| NO_CDK_FTTH |
| NO_LUM_FTTH |
| NO_TV |
| FTV_PRODUCT_DSL_GABFLAT |
| FTV_PRODUCT_TBB_GABFLAT |
| FTV_PRODUCT_COAX_GABFLAT |
| FTV_PRODUCT_CDK_FTTH_GABFLAT |
| FTV_PRODUCT_LUM_FTTH_GABFLAT |
| FTV_PRODUCT_TV_GABFLAT |
| NO_DSL_GABF |
| NO_TBB_GABF |
| NO_COAX_GABF |
| NO_CDK_FTTH_GABF |
| NO_LUM_FTTH_GABF |
| NO_TV_GABF |

- → [[CCM.ODS_GAB_ADD_INSTALL_SUBS_TEMP]]
| Column Name |
|---|
| LOAD_DTTM |
| GAB_FLAT |
| GAB_NUMBER |
| ADR_SEGMENT |
| ADR_TYPE_DETAIL2 |
| FTV_PRODUCT_DSL |
| FTV_PRODUCT_TBB |
| FTV_PRODUCT_COAX |
| FTV_PRODUCT_CDK_FTTH |
| FTV_PRODUCT_LUM_FTTH |
| FTV_PRODUCT_TV |
| NO_DSL |
| NO_TBB |
| NO_COAX |
| NO_CDK_FTTH |
| NO_LUM_FTTH |
| NO_TV |
| FTV_PRODUCT_DSL_GABFLAT |
| FTV_PRODUCT_TBB_GABFLAT |
| FTV_PRODUCT_COAX_GABFLAT |
| FTV_PRODUCT_CDK_FTTH_GABFLAT |
| FTV_PRODUCT_LUM_FTTH_GABFLAT |
| FTV_PRODUCT_TV_GABFLAT |
| NO_DSL_GABF |
| NO_TBB_GABF |
| NO_COAX_GABF |
| NO_CDK_FTTH_GABF |
| NO_LUM_FTTH_GABF |
| NO_TV_GABF |

- → [[CLM_CCM.ODS_PROCEDURE_SWAP_STATUS]]
| Column Name |
|---|
| PROCEDURE_NAME |
| EXECUTION_DATE |
| STATUS_MESSAGE |
| OLD_ROW_COUNT |
| NEW_ROW_COUNT |

- → [[CLM_CCM.CCM_LOAD_HISTORY]]
| Column Name |
|---|
| TABLE_NAME |
| START_DATE |
| STATUS |
| MESSAGE |
| POWERCENTER_WF_NAME |
| POWERCENTER_S_NAME |


