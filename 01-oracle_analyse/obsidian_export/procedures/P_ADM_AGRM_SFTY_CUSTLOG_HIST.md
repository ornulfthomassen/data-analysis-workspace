# P_ADM_AGRM_SFTY_CUSTLOG_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure incrementally loads and updates specific partitions within the `ADM_AGRM_SFTY_CUSTLOG_HIST` table. It processes new customer activity log data, specifically related to 'CUSTOMERLOG.ACTIVITY_LOG' and 'CUSTOMERLOG.ACTIVITY_LOG Bekreft e-post' events. For each target partition, it retrieves existing data and new activity data, combines them into a temporary table, and then uses a partition exchange operation to update the corresponding partition in the permanent historical table.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_AGRM_SFTY_CUSTLOG_HIST]]
| Column Name |
|---|
| KILDE |
| EVENT_ID |
| EVENT_DATE |
| CUSTOMER_SK |
| EVENT_DESCRIPTION |
| EVENT_TYPE_ID |
| EVENT_LEVEL1_ID |
| EVENT_LEVEL2_ID |
| EVENT_LEVEL3_ID |
| EVENT_LEVEL4_ID |
- ← [[CUSTOMERLOG.ACTIVITY_LOG]]
| Column Name |
|---|
| ACT_CUST_ID |
| INFO_REG_DATE |
| ACT_LOG_ID |
| DESCRIPTION_ID |
| ACT_EVENT_LEVEL1_ID |
| ACT_EVENT_LEVEL2_ID |
| ACT_EVENT_LEVEL3_ID |
| ACT_EVENT_LEVEL4_ID |
- ← [[CUSTOMERLOG.INTERNAL_CUSTOMER_LINK]]
| Column Name |
|---|
| ACT_CUST_ID |
| INFO_REG_DATE |
| INTERNAL_CUST_ID |
- ← [[CUSTOMERLOG.INTERNAL_CUSTOMER]]
| Column Name |
|---|
| INTERNAL_CUST_ID |
| INFO_IS_DELETED |
| CUST_ID |
- ← [[CM.CUSTOMER]]
| Column Name |
|---|
| KURT_ID |
| CUST_ID |
| INFO_IS_DELETED |
- ← [[CUSTOMERLOG.ACTIVITY_DESCRIPTION]]
| Column Name |
|---|
| DESCRIPTION_ID |
| DESCRIPTION_1 |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |

## Target Tables (Outputs)
- → [[ADM_AGRM_SFTY_CUSTLOG_HIST]]
| Column Name |
|---|
| KILDE |
| CUSTOMER_SK |
| EVENT_DATE |
| EVENT_DESCRIPTION |
| EVENT_ID |
| EVENT_TYPE_ID |
| EVENT_LEVEL1_ID |
| EVENT_LEVEL2_ID |
| EVENT_LEVEL3_ID |
| EVENT_LEVEL4_ID |
- → [[TMP_AGRM_SFTY_CUSTLOG_HIST0]]
| Column Name |
|---|
| KILDE |
| CUSTOMER_SK |
| EVENT_DATE |
| EVENT_DESCRIPTION |
| EVENT_ID |
| EVENT_TYPE_ID |
| EVENT_LEVEL1_ID |
| EVENT_LEVEL2_ID |
| EVENT_LEVEL3_ID |
| EVENT_LEVEL4_ID |
- → [[TMP_AGRM_SFTY_CUSTLOG_HIST0_2]]
| Column Name |
|---|
| KILDE |
| CUSTOMER_SK |
| EVENT_DATE |
| EVENT_DESCRIPTION |
| EVENT_ID |
| EVENT_TYPE_ID |
| EVENT_LEVEL1_ID |
| EVENT_LEVEL2_ID |
| EVENT_LEVEL3_ID |
| EVENT_LEVEL4_ID |
- → [[CRM_ANALYSE.LOG_TABLE]]

