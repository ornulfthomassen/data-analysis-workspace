# V_CM_DEVICE_AGREE_OWNR_CONFLCT

**Schema:** `CCM` | **Type:** `View`

## Description
Identifies recent orders (last 35 days) for a specific product offer (ID 76407) where the customer associated with the order offer is different from the customer who is the owner of the underlying agreement. This view highlights potential discrepancies or 'conflicts' in customer identity between the order placer and the agreement owner for certain device-related agreements.

## Data Sources (Inputs)
- ← [[ONL_REP.AGREEMENT_ORDER_OFFER]]
- ← [[ONL_REP.AGREEMENT_ORDER]]
- ← [[CM.CUSTOMER]]
- ← [[CM.AGREEMENT_OWNER]]

