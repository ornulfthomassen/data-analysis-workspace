# KIM_ORDER_STATUS_RANK_V

**Schema:** `CCM` | **Type:** `View`

## Description
Categorizes and assigns a numerical rank to order statuses based on their type code. It groups 'finished/archived' statuses as rank 1, 'in-progress/pending' statuses as rank 2, and all other statuses as rank 3.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_STATUS_DIM_MV]]

