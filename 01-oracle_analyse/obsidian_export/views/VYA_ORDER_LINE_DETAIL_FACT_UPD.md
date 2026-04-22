# VYA_ORDER_LINE_DETAIL_FACT_UPD

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides updated order line detail fact data, specifically focusing on mobile orders with 'Closed' or 'Cancelled' statuses. It uses a delta tracking mechanism (`CLM_ADM.ADM_DELTA_ORDER_SEQ_LOAD`) to identify and retrieve the most recent version of 'updated' records, effectively serving as an incremental update source for the core order line fact table.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_DELTA_ORDER_SEQ_LOAD]]
- ← [[CCM.VYAMN_ORDER_LINE_DETAIL_FACT]]
- ← [[GALAXY.ORDER_STATUS_DIM_MV]]

