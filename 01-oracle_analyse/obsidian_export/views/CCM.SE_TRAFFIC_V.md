# SE_TRAFFIC_V

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates monthly traffic data, calculating net traffic and total traffic volume. The view groups these metrics by period month, subscription key, main number, primary product name, and a traffic report group, applying filters for specific market areas and mobile telephony products.

## Data Sources (Inputs)
- ← [[GALAXY.TRAFFIC_MONTH_FACT_V]]
| Column Name |
|---|
| PERIODE_MONTH_KEY |
| SUBSCRIPTION_KEY |
| MAIN_NUMBER |
| TRAFFIC_NET_AMOUNT |
| TRAFFIC_NET_DISCOUNT_AMOUNT |
| TRAFFIC_VOLUME_TOTAL |
| PRIM_PRODUCT_KEY |
| TRAFFIC_TYPE_KEY |
| MARKET_AREA_KEY |

- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME |
| DRM_COMMON_PRODUCT_AREA |

- ← [[GALAXY.TRAFFIC_TYPE_DIM_V]]
| Column Name |
|---|
| TRAFFIC_TYPE_KEY |
| REPORT_GROUP_2 |


