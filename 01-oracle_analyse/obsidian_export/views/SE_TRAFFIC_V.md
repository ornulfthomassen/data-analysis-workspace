# SE_TRAFFIC_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates monthly traffic data, including net financial traffic and total traffic volume, for mobile telephony subscriptions within specific market areas (2 and 4). The data is grouped by month, subscription, main number, primary product name, and traffic report group, providing a detailed breakdown of mobile traffic performance.

## Data Sources (Inputs)
- ← [[galaxy.TRAFFIC_MONTH_FACT_V]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.TRAFFIC_TYPE_DIM_V]]

