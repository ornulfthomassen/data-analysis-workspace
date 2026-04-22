# VYA_ORDER_STATUS_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
This view, VYA_ORDER_STATUS_DIM, serves as an order status dimension table. Its primary function is to consolidate and categorize order status information, especially for 'MOBILE' business area orders, by deriving a simplified 'STATUS_CD' ('KB' for cancelled, 'FB' for finished/closed, 'IB' for in progress) based on a combination of existing status categories and types. This new STATUS_CD aims to standardize status representation for consumption by the Viya system, avoiding hardcoding in downstream applications. It provides a comprehensive set of order status attributes from its source.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_STATUS_DIM_MV]]

