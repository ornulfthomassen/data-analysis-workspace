# P_CCM_USER_SERVICES_PIVOT

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This procedure performs a full reload of a customer services pivot table by aggregating and transforming data from various usage and customer interaction sources. It first creates a new temporary table (`CCM_USER_SERVICES_PIVOT_N`) with the processed data, dynamically builds indexes on it, and then performs a table swap (using `ALTER TABLE RENAME`) to replace the existing permanent target table (`CCM_USER_SERVICES_PIVOT`) with the newly built one. The old permanent table is renamed as a backup (`CCM_USER_SERVICES_PIVOT_O`). A row count deviation check is implemented to prevent the table swap if the new data deviates significantly from the existing data, logging a warning in such cases. The procedure also manages grants on the new table and logs its execution status and any errors.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_USER_SERVICES_PIVOT]]
- ← [[CCDW_USAGE.OTT_SERVICES_USAGE_AGG]]
| Column Name |
|---|
| USER_CUSTOMER_ID |
| SOURCE_USER_ID |
| FIRST_ACCESS_DTM |
| LAST_ACCESS_DTM |
| OTT_SERVICE_ID |

- ← [[CCDW_USAGE.OTT_SERVICES]]
| Column Name |
|---|
| OTT_SERVICE_NAME |
| OTT_SERVICE_ID |

- ← [[ODS.CONNECT_ID_LINK]]
| Column Name |
|---|
| USER_ID |
| ACTIVE_FLAG |
| RANK_CONNECTION |
| RANK_CUSTOMER |
| CUST_LINK_QUALITY |
| CUSTOMER_ID |

- ← [[CLM_CCM.CCM_CUST_CHANNEL_INTERACTION]]
| Column Name |
|---|
| KURT_ID |
| APP_LAST_USED_DATE |
| APP_MEDIUM_LAST_USED |

- ← [[COMOYO.MINSKY_MAIN_DAILY]]
| Column Name |
|---|
| GLOBAL_ID |
| CREATION_TIME |
| LAST_FOREGROUND_DATE |
| LAST_FILE_EVENT_DTTM |
| LAST_CONNECTION_DTTM |
| USED_QUOTA |
| TOTAL_QUOTA |
| MEDIA_FILE_COUNT |
| LOAD_DATE |


## Target Tables (Outputs)
- → [[CLM_CCM.CCM_USER_SERVICES_PIVOT_N]]
| Column Name |
|---|
| KURT_ID |
| USER_ID |
| NBR_USERID |
| CUST_LINK_QUALITY |
| MINSKY_START |
| MINSKY_LAST |
| LAST_CONNECTION_DTTM |
| LAST_FILE_EVENT_DTTM |
| LAST_FOREGROUND_DATE |
| USED_QUOTA |
| TOTAL_QUOTA |
| MEDIA_FILE_COUNT |
| MITT_TELENOR_START |
| MITT_TELENOR_LAST |
| MITT_TELENOR_APP_VERSION |
| SE_HVEM_START |
| SE_HVEM_LAST |
| MINE_SIDER_START |
| MINE_SIDER_LAST |
| ONE_TELENOR_START |
| ONE_TELENOR_LAST |
| T_WE_START |
| T_WE_LAST |
| PRIVACY_SERVICES_START |
| PRIVACY_SERVICES_LAST |

- → [[CLM_CCM.CCM_USER_SERVICES_PIVOT]]
| Column Name |
|---|
| KURT_ID |
| USER_ID |
| NBR_USERID |
| CUST_LINK_QUALITY |
| MINSKY_START |
| MINSKY_LAST |
| LAST_CONNECTION_DTTM |
| LAST_FILE_EVENT_DTTM |
| LAST_FOREGROUND_DATE |
| USED_QUOTA |
| TOTAL_QUOTA |
| MEDIA_FILE_COUNT |
| MITT_TELENOR_START |
| MITT_TELENOR_LAST |
| MITT_TELENOR_APP_VERSION |
| SE_HVEM_START |
| SE_HVEM_LAST |
| MINE_SIDER_START |
| MINE_SIDER_LAST |
| ONE_TELENOR_START |
| ONE_TELENOR_LAST |
| T_WE_START |
| T_WE_LAST |
| PRIVACY_SERVICES_START |
| PRIVACY_SERVICES_LAST |

- → [[CLM_CCM.CCM_USER_SERVICES_PIVOT_O]]
- → [[CLM_CCM.CCM_LOAD_HISTORY]]
| Column Name |
|---|
| TABLE_NAME |
| START_DTTM |
| STATUS |
| ERROR_MESSAGE |
| POWERCENTER_WF_NAME |
| POWERCENTER_S_NAME |


