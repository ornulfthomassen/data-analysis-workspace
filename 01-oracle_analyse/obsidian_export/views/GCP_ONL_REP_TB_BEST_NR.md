# GCP_ONL_REP_TB_BEST_NR

**Schema:** `CCM` | **Type:** `View`

## Description
Retrieves the source order ID and sales ID (bestillingsnummer/order number) for agreements that originated from the 'Telenorbutikken' sales channel, filtering for orders placed within the last two complete calendar years relative to the current date and ensuring the sales ID is a valid number.

## Data Sources (Inputs)
- ← [[ONL_REP.AGREEMENT_ORDER]]
- ← [[GALAXY.DEALER_DIM]]

