# VYA_ORDER_LINE_REPLACEMENT

**Schema:** `CCM` | **Type:** `View`

## Description
This view, VYA_ORDER_LINE_REPLACEMENT, serves as a comprehensive analytical data set for order line details. It consolidates a vast array of information from a central order line fact table and enriches it with attributes from numerous dimension tables. The view provides detailed context for each order line, including product information (current, primary subscription, and from-order products), dates (order date, status date, regret dates), dealer and service provider details, order categories, order line types, order statuses, device information, and sales matrix data. It explicitly includes various Key Performance Indicators (KPIs) related to sales, churn, product changes, and other operational metrics, making it suitable for extensive reporting, analysis, and dashboard creation concerning order line performance and customer lifecycle events.

## Data Sources (Inputs)
- ← [[CCM.VYAMN_ORDER_LINE_DETAIL_FACT]]
- ← [[CCM.VYA_PRODUCT_DIM]]
- ← [[CCM.VYA_DATE_DIM]]
- ← [[CCM.VYA_DEALER_DIM]]
- ← [[GALAXY.ORDER_CATEGORY_DIM]]
- ← [[CCM.VYA_SERVICE_PROVIDER_DIM]]
- ← [[GALAXY.ORDER_LINE_TYPE_DIM]]
- ← [[CCM.VYA_ORDER_STATUS_DIM]]
- ← [[GALAXY.ORDER_STATUS_REASON_DIM_V]]
- ← [[CRM_ANALYSE.DEVICE_DIM_V]]
- ← [[GALAXY.SALES_MATRIX_DIM]]

