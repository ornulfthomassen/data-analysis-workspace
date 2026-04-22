# P_ADM_CONNECT_ID_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure P_ADM_CONNECT_ID_HIST populates monthly historical tables related to 'Connect IDs' (likely a unique identifier for a service or offering) by processing subscription and customer data. It builds three main partitioned historical tables: ADM_CONNECT_ID_HIST, ADM_CONNECT_ID_SUBSCR_HIST, and ADM_CONNECT_ID_CUST_HIST. For each target historical table, it first creates a temporary table, populates it with the relevant monthly data (derived from various source tables or previously built historical tables), and then uses an `ALTER TABLE ... EXCHANGE PARTITION` statement to efficiently swap the temporary table's data into a specific partition of the target historical table. Finally, it computes statistics for the new partition.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CM.SUBSCRIPTION]]
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY_I]]
- ← [[ADM_CONNECT_ID_HIST]]

## Target Tables (Outputs)
- → [[ADM_CONNECT_ID_HIST]]
- → [[TMP_CONNECT_ID]]
- → [[ADM_CONNECT_ID_SUBSCR_HIST]]
- → [[TMP_CONNECT_ID_SUBS]]
- → [[ADM_CONNECT_ID_CUST_HIST]]
- → [[TMP_CONNECT_ID_CUST]]

