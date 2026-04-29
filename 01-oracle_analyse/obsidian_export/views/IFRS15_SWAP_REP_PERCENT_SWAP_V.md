# IFRS15_SWAP_REP_PERCENT_SWAP_V

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates swap event statistics, including the total number of swapped contracts (categorized by 'D' and 'V' swap codes) and the percentage of contracts swapped, by joining contract details with swap event information and aggregating results by cohort, channel, business segment, and total contracts.

## Data Sources (Inputs)
- ← [[IFRS15.SWAP_REP_NUM_CONTRACTS_V]]
| Column Name |
|---|
| COHORT |
| CHANNEL |
| BUSINESS_SEGMENT |
| NUM_CONTRACTS |
| ACCOUNTING_MONTH |
| ACCOUNTING_YEAR |
- ← [[IFRS15.SWAP_REP_NUM_SWAP_EVENTS_V]]
| Column Name |
|---|
| SWAP_CODE |
| NUMBER_OF_SWAPEVENTS |
| CHANNEL |
| COHORT |
| BUSINESS_SEGMENT |
| ACCOUNTING_MONTH |
| ACCOUNTING_YEAR |

