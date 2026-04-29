# TMP_VIEW

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates various swap event metrics, including total swaps, specific 'D' and 'V' type swaps, and the percentage of total contracts that are swapped. These metrics are grouped by cohort, channel, business segment, and accounting period.

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
| NUMBER_OF_SWAPEVENTS |
| CHANNEL |
| COHORT |
| BUSINESS_SEGMENT |
| ACCOUNTING_MONTH |
| ACCOUNTING_YEAR |
| SWAP_CODE |

