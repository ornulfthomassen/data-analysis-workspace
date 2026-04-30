# V_NYSALG_SWAP_BINDING_CHURN

**Schema:** `CCM` | **Type:** `View`

## Description
This view analyzes mobile subscriptions that originated as 'new sales' ('NYSALG'), focusing on their lifecycle, contractual bindings, and product swap events. It filters for specific market areas and product groups (Mobile Postpaid), and excludes simple subscription transfers. The view calculates key metrics such as active days, days before binding, and days before a product swap, and provides detailed information about both the subscription and related swap activities.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MOBIL_SUBSCR_HIST]]
| Column Name |
|---|
| START_DATE |
| OWNER |
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| END_DATE |
| SUBSCR_START_REASON |
| MARKET_AREA_ID |
| PRODUCT_GROUP |
| SUBSCRIPTION_ID_PREV |

- ← [[GALAXY.SUBSCRIPTION_DIM]]
| Column Name |
|---|
| SUBSCRIPTION_KEY |
| PRIM_PROD_BIND_START_DT_KEY |
| PRIM_PROD_BIND_END_DT_KEY |
| PORT_IN_SERV_PROV_NAME |
| PORT_OUT_SERV_PROV_NAME |

- ← [[CRM_ANALYSE.ADM_HOUSEHOLD_INFO_KURT_HIST]]
| Column Name |
|---|
| KURT_ID |
| PERIOD_MONTH_KEY |
| AGE |

- ← [[ADHOC_BS.UK_1592_RES]]
| Column Name |
|---|
| MAIN_NUMBER |
| OLD_PRODUCT |
| NEW_PRODUCT |
| SALES_TYPE |
| SERVICE_PROVIDER_FROM |
| KPI_NEWSALE |
| SALES_MATRIX |
| AVT_NKR |
| ORDER_PROCESSED_DATE |
| KANAL_M0 |
| KJEDE_M0 |
| ORDER_ID |


