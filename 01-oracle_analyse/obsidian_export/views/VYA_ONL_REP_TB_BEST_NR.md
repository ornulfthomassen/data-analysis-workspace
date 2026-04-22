# VYA_ONL_REP_TB_BEST_NR

**Schema:** `CCM` | **Type:** `View`

## Description
Retrieves agreement order IDs and corresponding sales IDs for orders placed through the 'Telenorbutikken' sales channel, ensuring the sales ID is a valid number. It casts the agreement order ID to a VARCHAR2 string and the sales ID to a number.

## Data Sources (Inputs)
- ← [[ONL_REP.AGREEMENT_ORDER]]
- ← [[GALAXY.DEALER_DIM]]

