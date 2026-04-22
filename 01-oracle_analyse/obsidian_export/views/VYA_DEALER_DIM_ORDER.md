# VYA_DEALER_DIM_ORDER

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a filtered list of dealer dimension data. It includes all details for dealers (from the GALAXY.DEALER_DIM table) only if they have associated order line details in the GALAXY.ORDER_LINE_DETAIL_MOB_FACT_V view. Essentially, it identifies and presents dealers who have made orders.

## Data Sources (Inputs)
- ← [[GALAXY.DEALER_DIM]]
- ← [[GALAXY.ORDER_LINE_DETAIL_MOB_FACT_V]]

