# UPDATE_INACTIVE_MAIN_PROD_OLD

**Schema:** `CCM` | **Type:** `Procedure`

## Description
The procedure identifies subscriptions where the 'main product' information, as derived from the `CCDW` (Data Warehouse) and `CM` (Customer Management/Operational) systems, differs, or where the `CM` product is not classified as 'Mobil, HovedSIM'. It specifically focuses on active subscriptions in `CCDW` that show these discrepancies. It dynamically creates a temporary table (`TMP_INAKTIVT_HOVEDPRODUKT`) to stage the identified records. For each record in this temporary table, it updates the `CCM_SUBSCRIPTION` table, aligning its `MAIN_PRODUCT_ID`, `CONTACT_BRAND`, and `SUBSCRIPTION_TYPE` with the values from the `CM` system. All successful updates are logged into a permanent tracking table (`LOG_UPD_SUBSCR__MAIN_PROD`), which is also dynamically created if it does not exist.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |

- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| PRODUCT_OFFER_ID |
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| SOURCE_SYSTEM_ID |
| MARKET_AREA_ID |
| PARENT_SUBSCRIPTION_ID |
| ORIGINAL_START_DATE |
| START_DATE |

- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME |
| PRODUCT_BRAND |
| SOURCE_SYSTEM_NAME |
| SOURCE_PRODUCT_ID_1 |

- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SOURCE_SYSTEM_ID |
| SOURCE_SYSTEM_KEY |

- ← [[CM.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCR_ID |
| SUBSCR_VALID_TO_DATE |
| INFO_IS_DELETED |
| INFO_CHG_DATE |
| S212_PRODUCT_ID |

- ← [[STLOG.ST_IN]]
| Column Name |
|---|
| LAST_DATE_IN_LOAD_DATA |
| SOURCE_OBJECT |
| TARGET_OBJECT |
| START_BATCH |

- ← [[CCM.CCM_PRODUCT_TYPE_CONFIG]]
| Column Name |
|---|
| ID |
| PARENT |
| DESCRIPTION |

- ← [[CCDW.SUBSCRIBED_PRODUCT]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PRODUCT_OFFER_ID |
| END_DATE |

- ← [[CCM.TMP_INAKTIVT_HOVEDPRODUKT]]
| Column Name |
|---|
| MAIN_NUMBER |
| SUBSCRIPTION_ID |
| CCDW_PRODUCT_OFFER_ID |
| CCDW_PRODUCT_NAME |
| CCDW_PRODUCT_BRAND |
| CCDW_PRODUCT_TYPE |
| CM_PRODUCT_OFFER_ID |
| CM_PRODUCT_NAME |
| CM_PRODUCT_BRAND |
| CM_PRODUCT_TYPE |


## Target Tables (Outputs)
- → [[CCM.LOG_UPD_SUBSCR__MAIN_PROD]]
| Column Name |
|---|
| UPD_DTTM |
| UPD_MONTH_KEY |
| UPD_DT_KEY |
| MAIN_NUMBER |
| SUBSCRIPTION_ID |
| FROM_PRODUCT_OFFER_ID |
| FROM_PRODUCT_NAME |
| FROM_SUBSCRIPTION_TYPE |
| TO_PRODUCT_OFFER_ID |
| TO_PRODUCT_NAME |
| TO_SUBSCRIPTION_TYPE |
| SUKSESS |
| FROM_PRODUCT_BRAND |
| TO_PRODUCT_BRAND |

- → [[CCM.TMP_INAKTIVT_HOVEDPRODUKT]]
| Column Name |
|---|
| CM_PRODUCT_NAME |
| CM_PRODUCT_OFFER_ID |
| CM_PRODUCT_BRAND |
| CM_SOURCE_SYSTEM_NAME |
| S212_PRODUCT_ID |
| CM_PRODUCT_TYPE |
| CCDW_PRODUCT_NAME |
| CCDW_PRODUCT_OFFER_ID |
| CCDW_PRODUCT_BRAND |
| CCDW_SOURCE_SYSTEM_NAME |
| SOURCE_PRODUCT_ID_1 |
| CCDW_PRODUCT_TYPE |
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| SOURCE_SYSTEM_KEY |
| ORIGINAL_START_DATE |
| START_DATE |
| INFO_CHG_DATE |
| RUN_TIME |

- → [[CCM.CCM_SUBSCRIPTION]]
| Column Name |
|---|
| MAIN_PRODUCT_ID |
| CONTACT_BRAND |
| SUBSCRIPTION_TYPE |


