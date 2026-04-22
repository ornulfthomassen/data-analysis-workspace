# GCP_HARDWARE_ORDER_EVENTS

**Schema:** `CCM` | **Type:** `View`

## Description
This view, GCP_HARDWARE_ORDER_EVENTS, provides a comprehensive and consolidated dataset of recent hardware orders placed through the Telenor online store ('nettbutikken telenor.no'). It extracts core hardware order details, customer information, associated service and agreement orders (including specifics on SWAP, Insurance, and Downpayment products), and detailed product specifications (manufacturer, model, size, color, GTIN). The view filters for standard B2C orders from the last 3 months, focusing on 'processing' or recently 'finished' statuses. It aggregates various product parameters, translates status and material category codes into human-readable descriptions, and prepares this enriched data for analytical purposes, specifically for loading into the Viya platform.

## Data Sources (Inputs)
- ← [[ONL_HW_ORDERS_REP.HARDWARE_ORDER]]
- ← [[CM.CUSTOMER]]
- ← [[FPS.TERMINAL_GTIN_PROPERTIES]]
- ← [[ONL_HW_ORDERS_REP.HARDWARE_ORDER_PRODUCT_PARAM]]
- ← [[ONL_REP.SERVICE_ORDER]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
- ← [[ONL_REP.SUBSCRIBED_OFFER_ORDER]]
- ← [[CLM_ADM.ADM_PRODUCT_ATTRIBUTE_HIST]]
- ← [[ONL_REP.AGREEMENT_ORDER]]
- ← [[ONL_REP.AGREEMENT_ORDER_OFFER]]
- ← [[CM.AGREEMENT_OFFER]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.ORDER_STATUS_DIM_MV]]

