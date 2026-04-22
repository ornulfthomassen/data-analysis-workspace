# PORT_ORDER_LINE_DETAIL_FACT_V

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates order line details for specific 'porting' related orders (identified by ORDER_LINE_TYPE_KEYs 17, 18 and SOURCE_SYSTEM_KEY 24) that are linked to active subscriptions in market areas 2 or 4. It summarizes various order attributes, such as customer and source order IDs, important dates, service provider and customer keys, product keys, subscription ID, and main number, while also providing a count of lines within each aggregated order.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
- ← [[CCDW.SUBSCRIPTION]]

