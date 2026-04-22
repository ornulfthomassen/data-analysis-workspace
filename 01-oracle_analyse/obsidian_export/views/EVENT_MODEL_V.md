# EVENT_MODEL_V

**Schema:** `CCM` | **Type:** `View`

## Description
Consolidates various customer-centric events (personalized campaigns, customer service calls, and order details) into a unified view for analytical purposes. It standardizes event attributes like date, type, category, related activity, campaign, channel, and various key performance indicators (KPIs) such as sales, swaps, and product changes.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT_V]]
- ← [[kim_channel_dim]]
- ← [[CRM_ANALYSE.KS_INTERACTION]]
- ← [[galaxy.order_line_detail_fact_mv]]
- ← [[GALAXY.ORDER_LINE_TYPE_DIM]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[GALAXY.ORDER_TIME_DIM_V]]

