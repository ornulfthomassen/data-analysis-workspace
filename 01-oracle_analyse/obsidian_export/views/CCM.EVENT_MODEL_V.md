# EVENT_MODEL_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view unifies various customer interactions and events—including personalized campaign engagements, customer service calls, and detailed order transactions—into a single, standardized analytical dataset. It normalizes event attributes and calculates key performance indicators (KPIs) across these disparate data sources for comprehensive CRM analysis, effectively creating a consolidated 'event model' for analytical purposes.

## Data Sources (Inputs)
- ← [[CCM.KIM_CAMPAIGN_DETAIL_FACT_V]]
| Column Name |
|---|
| CONTACT_KEY |
| CONTACT_DTTM |
| CAMPAIGN_TYPE_DESC |
| CAMPAIGN_SYSTEM |
| ACTIVITY_MAIN_OBJECTIVE |
| PROGRAM |
| ACTIVITY_ID |
| ACTIVITY_DESC |
| CAMPAIGN |
| CAMPAIGN_DESC |
| CHANNEL_KEY |
| SALES_MATRIX |
| KPI_SALES |
| KPI_ALL_SALES |
| KPI_SWAP |
| EFFECT_RANK |
| EFFECT_TYPE |
| KPI_ACCEPTED |
| MAIN_NUMBER |
| KURT_ID_OWNER |
| CONTACT_DATE_KEY |

- ← [[CCM.KIM_CHANNEL_DIM]]
| Column Name |
|---|
| CHANNEL_KEY |
| CHANNEL_COMMON_NM |

- ← [[CRM_ANALYSE.KS_INTERACTION]]
| Column Name |
|---|
| INTERACTION_SEGMENT_ID |
| START_CAL_DATE |
| QUEUE_TYPE |
| TECHNICAL_RESULT |
| CALLED_SERVICE |
| QUEUE_PROGRAM |
| SITE_NAME |
| KEYED_NUMBER_NUM |
| CALL_FROM_NUM |
| KURT_ID_OWNER |
| HANDLE_COUNT |

- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
| Column Name |
|---|
| SOURCE_ORDER_ID |
| ORDER_DT_KEY |
| ORDER_LINE_TYPE_KEY |
| ORDERLINE_PRODUCT_KEY |
| FROM_ORDER_PRODUCT_KEY |
| DEALER_KEY |
| KPI_PRODUCT_CHANGE |
| KPI_NEWSALE |
| KPI_PORTING_INBOUND |
| KPI_PORTING_OUTBOUND |
| KPI_TERMINATION |
| RESOURCE_VALUE |
| OWNER_CUSTOMER_KEY |
| MARKET_AREA_KEY |

- ← [[GALAXY.ORDER_LINE_TYPE_DIM]]
| Column Name |
|---|
| ORDERLINE_TYPE_KEY |
| ORDERLINE_TYPE_DESC |

- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
| PRODUCT_NAME |
| PRODUCT_DESC |
| PRODUCT_FAMILY_NAME |
| DRM_COMMON_PRODUCT_AREA |
| TK_INCOME_SERVICE |
| PRODUCT_PAYTYPE |
| TK_PRODUCT_RANK |
| PRODUCT_BRAND |

- ← [[GALAXY.DEALER_DIM]]
| Column Name |
|---|
| DEALER_KEY |
| DRM_SALES_CHANNEL_GEN04_DESC |

- ← [[GALAXY.ORDER_TIME_DIM_V]]
| Column Name |
|---|
| ORDER_TIME_KEY |
| ORDER_TIME |


