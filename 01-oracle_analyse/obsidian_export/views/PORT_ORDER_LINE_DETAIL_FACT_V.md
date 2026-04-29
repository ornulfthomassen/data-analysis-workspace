# PORT_ORDER_LINE_DETAIL_FACT_V

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates and filters order line detail facts from the `ORDER_LINE_DETAIL_FACT_MV` table, linking them to specific subscription criteria from the `SUBSCRIPTION` table. The view consolidates various order-related attributes (like dates, customer keys, service providers, status, product, subscription ID, and main number) for each `ORDER_KEY`, applying various aggregation functions including `MIN`, `MAX`, and `KEEP (DENSE_RANK FIRST ORDER BY SOURCE_SYSTEM_KEY)`. It specifically targets orders with certain `ORDER_LINE_TYPE_KEY` values, a minimum `ORDERING_DT_KEY`, a particular `SOURCE_SYSTEM_KEY`, and ensures the associated `SUBSCRIPTION_ID` is active within specific `MARKET_AREA_ID`s at the time of ordering.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
| Column Name |
|---|
| ORDER_KEY |
| SOURCE_SYSTEM_KEY |
| CUSTOMER_ORDER_ID |
| SOURCE_ORDER_ID |
| ORDER_DT_KEY |
| ORDERING_DT_KEY |
| ORDER_STATUS_DT_KEY |
| WANTED_DELIVERY_DT_KEY |
| AGREED_DELIVERY_DT_KEY |
| SERVICE_PROVIDER_FROM_KEY |
| SERVICE_PROVIDER_TO_KEY |
| OWNER_CUSTOMER_KEY |
| USER_CUSTOMER_KEY |
| PORT_CASE_ID |
| ORDER_LINE_TYPE_KEY |
| ORDER_STATUS_KEY |
| ORDER_STATUS_REASON_KEY |
| ORDERLINE_PRODUCT_KEY |
| ORDERLINE_SUBSCR_KEY |
| RESOURCE_VALUE |
- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MARKET_AREA_ID |
| END_DATE |

