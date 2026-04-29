# VYA_ODS_AGRMT_OFFER_MOB_RW_AG

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies and prioritizes the most relevant reward offer for each agreement by applying a ranking mechanism. It selects a single 'best' offer per agreement based on criteria like reward status (active preferred), allocated GB sum (highest preferred), and agreement offer ID, filtering out other offers or specific problematic agreement IDs.

## Data Sources (Inputs)
- ← [[CLM_CCM.V_ODS_AGRMT_MOB_REWARD_AGG]]
| Column Name |
|---|
| AGREEMENT_ID |
| SRC_AGRM_AGREEMENT_OFFER_ID |
| REWARD_STATUS |
| REWARD_NO_UNITS_BASIS |
| REWARD_NO_UNITS_CAN_USE |
| REWARD_ALLOCATED_GB_SUM |
| REWARD_NO_MPP |
| REWARD_NO_AGREEMENT |
| REWARD_NO_FIXED |
| REWARD_NO_MOBILE |
| AGRM_NO_PERSONS |
| AGRM_NO_PERSONS_CONTRIB |

