# VYA_ODS_AGRMT_OFFER_MOB_RW_AG

**Schema:** `CCM` | **Type:** `View`

## Description
This view selects the most relevant mobile reward offer for each agreement. It prioritizes offers based on 'REWARD_STATUS' (preferring active offers), then by 'REWARD_ALLOCATED_GB_SUM' (preferring higher values), and finally by 'SRC_AGRM_AGREEMENT_OFFER_ID' for tie-breaking. The view extracts various reward and agreement-related metrics, excluding specific problematic agreement IDs, and is intended for loading ODS agreement reward data.

## Data Sources (Inputs)
- ← [[CLM_CCM.V_ODS_AGRMT_MOB_REWARD_AGG]]

