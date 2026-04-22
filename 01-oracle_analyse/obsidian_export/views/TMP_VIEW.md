# TMP_VIEW

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates the total number of contracts, total swap events, and specific types of swap events (identified by 'D' and 'V' swap codes), along with the percentage of total swap events relative to total contracts. The metrics are aggregated and presented for each unique combination of cohort, channel, and business segment within specific accounting months and years.

## Data Sources (Inputs)
- ← [[IFRS15.SWAP_REP_NUM_CONTRACTS_V]]
- ← [[IFRS15.SWAP_REP_NUM_SWAP_EVENTS_V]]

