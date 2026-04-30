# P_CCM_USER_SERVICES_DIM

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Populates or refreshes the `CCM_USER_SERVICES_DIM` table with aggregated user service data. It summarizes user service activity from `COMOYO.USER_SERVICES_SERVICE` and `ODS.CONNECT_ID_LINK` over the last 35 days, categorizes service names, counts their occurrences, and then merges this data into the `CCM_USER_SERVICES_DIM` table, updating existing entries or inserting new ones.

## Data Sources (Inputs)
- ← [[COMOYO.USER_SERVICES_SERVICE]]
| Column Name |
|---|
| SERVICE_NAME |
| LAST_ACCESS_TM |
| USER_ID |

- ← [[ODS.CONNECT_ID_LINK]]
| Column Name |
|---|
| USER_ID |
| RANK_CONNECTION |
| ACTIVE_FLAG |

- ← [[CCM.CCM_USER_SERVICES_DIM]]
| Column Name |
|---|
| SERVICE_CD |


## Target Tables (Outputs)
- → [[CCM.TMP_USER_SERVICES_DIM]]
| Column Name |
|---|
| SERVICE_CD |
| SERVICE_NAME |
| ANTALL |
| SERVICE_OF_INTEREST |

- → [[CCM.CCM_USER_SERVICES_DIM]]
| Column Name |
|---|
| SERVICE_CD |
| SERVICE_NAME |
| ANTALL |
| SERVICE_OF_INTEREST |


