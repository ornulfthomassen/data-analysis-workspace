# VYA_INSIGHT_DEVICE_FROM_ORDER

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates and consolidates device-centric order and service history, identified by IMEI. It combines agreement order details and service order details, enriching them with customer information (owner and user) and various product-related KPIs (e.g., swaps, insurance, product changes, commissions). The view provides aggregated historical data points such as min/max order IDs, dates, market areas, and dealer keys for each unique device (IMEI).

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[GALAXY.ORDER_LINE_DETAIL_MOB_FACT_MV]]
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
- ← [[PD]]

