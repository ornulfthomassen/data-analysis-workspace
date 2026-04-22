# VYA_COMMISSION_DETAIL

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates and aggregates detailed commission information for orders. It provides a comprehensive breakdown including product details, associated dealers (employee, commission, receiver), various commission amounts (gross and net), units, unit price, relevant dates (ordering, first/last/list payment), and voucher IDs. It links these commission details to order-level information such as source order ID, IMEI, handset key, and subscription master data to offer a holistic view of commissions related to specific orders and products.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[CCDW_COMMISSIONS.COMMISSION_DETAIL]]
- ← [[CCDW_COMMISSIONS.COMMISSION_PRODUCT]]
- ← [[CCDW_COMMISSIONS.COMMISSION_CATEGORY]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]

