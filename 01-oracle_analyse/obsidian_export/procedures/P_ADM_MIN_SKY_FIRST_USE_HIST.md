# P_ADM_MIN_SKY_FIRST_USE_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure identifies and inserts new 'first use' events for users into the `ADM_MIN_SKY_FIRST_USE_HIST` table. It collects usage events from `COMOYO.COMOYO_SUB_GRANT_EVENTS`, filters out records already present in the history table, determines the earliest event time, load date, and SKU for each user and grantor combination, stores these in a temporary table (`TMP_MIN_SKY_FIRST_USE_HIST`), and then loads them into the permanent history table. It includes checks for table existence, dynamic table creation/dropping, and error handling for insert failures.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
- ← [[COMOYO.COMOYO_SUB_GRANT_EVENTS]]
| Column Name |
|---|
| USER_ID |
| GRANTOR |
| EVENT_TIME |
| LOAD_DATE |
| SKUS |
| EVENT |
- ← [[ADM_MIN_SKY_FIRST_USE_HIST]]
| Column Name |
|---|
| GLOBAL_ID_CHAR |
| GRANTOR |
- ← [[TMP_MIN_SKY_FIRST_USE_HIST]]
| Column Name |
|---|
| USER_ID |
| GRANTOR |
| FIRST_EVENT_DTTM |
| FIRST_LOAD_DATE |
| SKUS |

## Target Tables (Outputs)
- → [[TMP_MIN_SKY_FIRST_USE_HIST]]
| Column Name |
|---|
| USER_ID |
| GRANTOR |
| FIRST_EVENT_DTTM |
| FIRST_LOAD_DATE |
| SKUS |
- → [[ADM_MIN_SKY_FIRST_USE_HIST]]
| Column Name |
|---|
| GLOBAL_ID_CHAR |
| GLOBAL_ID |
| GRANTOR |
| FIRST_EVENT_DTTM |
| FIRST_LOAD_DATE |
| SKUS |

