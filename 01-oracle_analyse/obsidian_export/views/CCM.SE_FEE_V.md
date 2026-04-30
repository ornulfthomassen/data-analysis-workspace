# SE_FEE_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates subscription fee data by month, subscription, main number, and product details. It calculates total net fees (summing initiation, periodic, and discount fees) and net termination fees for 'Mobil Telefoni' (Mobile Telephony) products within specific market areas (2 and 4).

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_FEE_MONTH_FACT_V]]
| Column Name |
|---|
| PERIODE_MONTH_KEY |
| SUBSCRIPTION_KEY |
| PRIM_PRODUCT_KEY |
| SUB_PRODUCT_KEY |
| NET_INITIATION_FEE |
| NET_PERIODIC_FEE |
| NET_DISCOUNT_FIXED_FEE |
| NET_DISCOUNT_STARTUP_FEE |
| NET_TERMINATION_FEE |
| MARKET_AREA_KEY |

- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_MARKET_PRODUCT |
| DRM_COMMON_PRODUCT_AREA |

- ← [[GALAXY.SUBSCRIPTION_DIM_MV]]
| Column Name |
|---|
| SUBSCRIPTION_KEY |
| MAIN_NUMBER |


