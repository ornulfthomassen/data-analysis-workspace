# SE_NET_REV_WO_BIND_V

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates the aggregated net revenue components (initiation, periodic, and discount fees) for mobile telephony subscriptions within specific market areas (2 and 4), excluding any revenue associated with 'Terminalbinding' type sub-products. The results are grouped by period month and subscription key.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_FEE_MONTH_FACT_V]]
| Column Name |
|---|
| PERIODE_MONTH_KEY |
| SUBSCRIPTION_KEY |
| NET_INITIATION_FEE |
| NET_PERIODIC_FEE |
| NET_DISCOUNT_FIXED_FEE |
| NET_DISCOUNT_STARTUP_FEE |
| PRIM_PRODUCT_KEY |
| SUB_PRODUCT_KEY |
| MARKET_AREA_KEY |

- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| DRM_COMMON_PRODUCT_AREA |
| PRODUCT_BINDING_TYPE_NAME |

- ← [[GALAXY.SUBSCRIPTION_DIM_MV]]
| Column Name |
|---|
| SUBSCRIPTION_KEY |


