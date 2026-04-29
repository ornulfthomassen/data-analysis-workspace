# P_ADM_FB_COUNTS_CUST_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure processes customer product counts for a specified month (P_YYYYMM), aggregates various product subscriptions from source tables, and stores the results in a partitioned historical table called ADM_FB_COUNTS_CUST_HIST. It performs checks for source data availability and existing partitions, creates a temporary table for intermediate calculations, and then exchanges the temporary table with a new partition in the main historical table. It also logs its execution status and errors.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[AGR.BMGM_COUNTS_KURT]]
| Column Name |
|---|
| SEQ_ID |
| KURT_ID |
| NUM_PRIV_POSTPAID_SUBS_OWNED |
| NUM_BUS_POSTPAID_SUBS_USED |
| NUM_SWAP_AGREEMENTS_OWNED |
| NUM_MBB_SUBS_OWNED |
| NUM_FIXED_BROADBAND_OWNED |
| NUM_FIXED_TELEPHONY_SUBS_OWNED |
- ← [[STLOG.ST_IN]]
| Column Name |
|---|
| SEQ_ID |
| START_BATCH |
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |
- ← [[ADM_FB_COUNTS_CUST_HIST]]

## Target Tables (Outputs)
- → [[TMP_FB_COUNTS_CUST_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK |
| NUM_FB_PRODUCTS |
| NUM_PRIV_POSTPAID_SUBS_OWNED |
| NUM_BUS_POSTPAID_SUBS_USED |
| NUM_SWAP_AGREEMENTS_OWNED |
| NUM_MBB_SUBS_OWNED |
| NUM_FIXED_BROADBAND_OWNED |
| NUM_FIXED_TELEPHONY_SUBS_OWNED |
- → [[ADM_FB_COUNTS_CUST_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK |
| NUM_FB_PRODUCTS |
| NUM_PRIV_POSTPAID_SUBS_OWNED |
| NUM_BUS_POSTPAID_SUBS_USED |
| NUM_SWAP_AGREEMENTS_OWNED |
| NUM_MBB_SUBS_OWNED |
| NUM_FIXED_BROADBAND_OWNED |
| NUM_FIXED_TELEPHONY_SUBS_OWNED |
- → [[CRM_ANALYSE.ADM_LOAD_HISTORY]]
| Column Name |
|---|
| TABLE_NAME |
| PERIOD_MONTH_KEY |
| STATUS |
| MESSAGE |

