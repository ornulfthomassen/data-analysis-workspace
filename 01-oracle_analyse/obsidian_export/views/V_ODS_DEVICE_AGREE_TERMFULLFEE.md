# V_ODS_DEVICE_AGREE_TERMFULLFEE

**Schema:** `CCM` | **Type:** `View`

## Description
Retrieves recent device agreement order details, including customer and account identifiers, a specific agreement parameter value (either 'S' or 'P'), and the device's IMEI. It filters for orders of type 770 that have arrived within the last three days.

## Data Sources (Inputs)
- ← [[ONL_REP.AGREEMENT_ORDER]]
- ← [[ONL_REP.AGREEMENT_ORDER_COMPONENT]]
- ← [[ONL_REP.AGREEMENT_ORDER_COMP_PARAM]]
- ← [[ONL_REP.AGREEMENT_ORDER_OFFER]]
- ← [[CM.CUSTOMER]]

