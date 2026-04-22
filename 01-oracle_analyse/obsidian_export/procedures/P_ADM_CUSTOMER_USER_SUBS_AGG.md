# P_ADM_CUSTOMER_USER_SUBS_AGG

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `P_ADM_CUSTOMER_USER_SUBS_AGG` is designed to aggregate customer subscription and usage statistics on a monthly basis for a specified period (`P_YYYYMM`). It first performs a preliminary check to ensure all necessary source data for the given month is available. If the source data is sufficient, it constructs a large SQL query to calculate various metrics (fees, usage, product-group specific counts, activity days, traffic data like MB, MMS, SMS, Voice for multiple previous periods) by joining several historical and aggregated tables related to customer information, subscriptions, and products. This aggregated data is initially stored in a temporary table (`TMP_CUSTOMER_USER_SUBS_AGG`). Finally, it uses a partition exchange mechanism (`ALTER TABLE ... EXCHANGE PARTITION`) to efficiently load this data from the temporary table into a designated monthly partition of a permanent analytical table (`ADM_CUSTOMER_USER_SUBS_AGG`), handling creation of the partition if it doesn't exist and managing overwrite logic. The procedure also includes robust error handling and logging.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CLM_ADM.ADM_SUBSCR_DETAIL_HIST]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_AGG]]
- ← [[PD]]

## Target Tables (Outputs)
- → [[ADM_CUSTOMER_USER_SUBS_AGG]]
- → [[TMP_CUSTOMER_USER_SUBS_AGG]]

