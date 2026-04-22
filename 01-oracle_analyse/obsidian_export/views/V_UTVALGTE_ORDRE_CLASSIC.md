# V_UTVALGTE_ORDRE_CLASSIC

**Schema:** `CCM` | **Type:** `View`

## Description
This view extracts detailed information for a selection of 'classic' orders, applying extensive filters. It retrieves order-related attributes such as day, customer key, product name and description, customer order type, order action type and reason, order status name and reason. The selection criteria include specific product names ('60272', '60110'), various customer order types (e.g., termination, resale, product change, new account), specific order action types ('NEW', 'CANCELLED'), certain order statuses (e.g., 'PENDING', 'STARTED'), specific market areas ('PRIVATE', 'PRIVATE BUSINESS'), and excludes orders from 'BA Norway Datterselskaper' and 'BA Norway Telenor Norge' counterpart classifications. It also filters for year-to-date data.

## Data Sources (Inputs)
- ← [[ORDER_DT_DIM_V]]
- ← [[SUBSCR_USER_DIM_V]]
- ← [[ORDER_LINE_PRODUCT_DIM_V]]
- ← [[SALES_ORDER_INDICATOR_DIM_MV]]
- ← [[ORDER_STATUS_DIM_MV]]
- ← [[ORDER_STATUS_REASON_DIM_V]]
- ← [[COUNTERPART_OWNER_DIM_V]]
- ← [[MARKET_AREA_DIM]]
- ← [[ORDER_DETAIL_FACT_V]]
- ← [[SUBSCR_OWNER_DIM_V]]

