# BALANCE01_TALKMORE_AGG

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure manages and populates a partitioned aggregation table for 'Talkmore' subscription balances. It dynamically creates the target table 'CLM_ADM.BALANCE_TALKMORE_AGG' if it doesn't exist, initializing it as a partitioned table with initial partitions. For a specified range of months (or the previous month by default), it iterates through each month, drops any existing partition for that month, and then re-creates a new partition. It then calculates and inserts aggregated data, specifically the distinct count of `DIRECTORY_NUMBER_ID` for 'Talkmore' subscriptions (identified by product description containing 'TALKMORE'), categorized by product description and payment type (Prepaid/Postpaid), for each month into the respective partitions. This process effectively maintains a historical summary of 'Talkmore' subscription counts, refreshing data for the specified periods.

## Data Sources (Inputs)
- ← [[CM.SUBSCRIPTION]]
- ← [[CM.PROD_SERV_MAPPING]]
- ← [[GALAXY.DATE_DIM_MV]]

## Target Tables (Outputs)
- → [[CLM_ADM.BALANCE_TALKMORE_AGG]]

