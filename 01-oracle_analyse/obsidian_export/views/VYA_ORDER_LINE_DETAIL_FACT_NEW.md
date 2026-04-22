# VYA_ORDER_LINE_DETAIL_FACT_NEW

**Schema:** `CCM` | **Type:** `View`

## Description
This view extracts detailed order line fact records, focusing on new or updated entries. It specifically retrieves order line data for the 'MOBILE' business area where orders have a 'CLOSED' or 'CANCELLED' status. The view incorporates an incremental loading mechanism, using a delta tracking table (`ADM_DELTA_ORDER_SEQ_LOAD`) to identify and process only the latest unprocessed batches of order data, linking them to the main order line fact table and an order status dimension.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_DELTA_ORDER_SEQ_LOAD]]
- ← [[CCM.VYAMN_ORDER_LINE_DETAIL_FACT]]
- ← [[GALAXY.ORDER_STATUS_DIM_MV]]

