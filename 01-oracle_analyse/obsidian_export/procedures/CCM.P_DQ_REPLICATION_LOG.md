# P_DQ_REPLICATION_LOG

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Logs the maximum 'info_chg_date' and its freshness (difference from current date/time) for the last 4 days from three specific CM schema tables (SUBSCRIPTION, SUBSCRIPTION_OFFER_INCENTIVE, AGREEMENT_NEW) into the DQ_REPLICATION_LOG table. This likely serves as a replication or data quality check.

## Data Sources (Inputs)
- ← [[CM.SUBSCRIPTION]]
| Column Name |
|---|
| info_chg_date |

- ← [[CM.SUBSCRIPTION_OFFER_INCENTIVE]]
| Column Name |
|---|
| info_chg_date |

- ← [[CM.AGREEMENT_NEW]]
| Column Name |
|---|
| info_chg_date |


## Target Tables (Outputs)
- → [[CCM.DQ_REPLICATION_LOG]]
| Column Name |
|---|
| max_info_chg_date |
| check_date_time |
| diff |
| check_table |


