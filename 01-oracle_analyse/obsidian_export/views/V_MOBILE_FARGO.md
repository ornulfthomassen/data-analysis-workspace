# V_MOBILE_FARGO

**Schema:** `CCM` | **Type:** `View`

## Description
This view, V_MOBILE_FARGO, consolidates and transforms mobile service order data to identify and categorize key performance indicators (KPIs) related to different types of order actions. It calculates indicators for new sales (KPI_NYSALG), product changes (KPI_PRODUCT_CHANGE), and ownership changes (KPI_OWNERCHANGE) based on specific order and product action types. The view provides comprehensive details about service orders, including order IDs, statuses, dates, associated dealer, customer types, product information (current, previous, and offers), subscription details, and enriched sales channel attributes. It aims to provide a unified dataset for reporting or analysis of mobile service provisioning, sales performance, and customer actions.

## Data Sources (Inputs)
- ← [[ONL_REP.SERVICE_ORDER]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
- ← [[ONL_REP.SUBSCRIBED_OFFER_ORDER]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[ODS.SUBSCRIPTION_ODS_MOB]]
- ← [[CLM_CCM.V_CCM_DEALER_DIM]]

