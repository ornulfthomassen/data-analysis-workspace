# PORTING_INBOUND_IB_V

**Schema:** `CCM` | **Type:** `View`

## Description
Retrieves recent service order details for new sales and port-in actions related to GSM products. It combines core order and product information with specific customer IDs (owner, payer, user 'Kurt IDs') associated with those orders. The view primarily focuses on orders with a 'New Sale' action type and 'Port In' product action type for private customers, processed or arrived recently (within the last day).

## Data Sources (Inputs)
- ← [[ONL_REP.SERVICE_ORDER]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
- ← [[CLM_RTDM.V_ONL_SERVICE_ORDER]]
- ← [[CLM_RTDM.V_ONL_SERVICE_ORDER_CUSTOMER]]

