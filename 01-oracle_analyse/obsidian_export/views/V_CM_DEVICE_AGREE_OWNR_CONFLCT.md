# V_CM_DEVICE_AGREE_OWNR_CONFLCT

**Schema:** `CCM` | **Type:** `View`

## Description
Identifies agreement orders where the customer associated with the order has a different 'KURT_ID' than the customer designated as the agreement owner. The view filters for recent orders (last 35 days), a specific product offer (76407), and primary agreement offers, indicating a potential conflict in customer identification between the order and agreement ownership.

## Data Sources (Inputs)
- ← [[ONL_REP.AGREEMENT_ORDER_OFFER]]
| Column Name |
|---|
| AGREEMENT_ORDER_ID |
| CUST_ID |
| PRODUCT_OFFER_ID |
| AGREEMENT_OFFER_ID_PARENT |
- ← [[ONL_REP.AGREEMENT_ORDER]]
| Column Name |
|---|
| STATUS_ID |
| SALES_ID |
| AGREEMENT_ORDER_ID |
| ORDER_ARRIVAL_DATE |
| AGREEMENT_ID |
- ← [[CM.CUSTOMER]]
| Column Name |
|---|
| KURT_ID |
| CUST_ID |
| CUST_FIRST_NAME |
| CUST_LAST_NAME |
| MASTER_ID |
- ← [[CM.AGREEMENT_OWNER]]
| Column Name |
|---|
| AGREEMENT_ID |
| MASTER_ID |

