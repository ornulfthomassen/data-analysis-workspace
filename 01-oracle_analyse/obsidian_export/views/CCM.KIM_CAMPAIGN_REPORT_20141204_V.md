# KIM_CAMPAIGN_REPORT_20141204_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive campaign performance report by aggregating and calculating various Key Performance Indicators (KPIs) such as sales volume, presented, accepted, selected, and new sale volumes. It combines detailed campaign contact data with information from various dimension tables, including order ranks, response types, communication details, churn groups, and product configurations. The report is filtered by measure type and contact month, and it also derives a 'Sales Matrix' categorization based on product changes.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| VOLUME |
| ORDER_RANK |
| SOURCE_SYSTEM_KEY |
| CONTACT_DTTM |
| ORDER_FROM_PRODUCT_KEY |
| ORDER_TO_PRODUCT_KEY |
| CONTACT_KEY |
| CONN_ID |
| MEASURE_TYPE |
| CHANNEL_KEY |
| CAMPAIGN_KEY |
| COMMUNICATION_KEY |
| TREATMENT_KEY |
| TREATMENT_PRIORITY |
| CONTACT_DATE_KEY |
| CONTACT_MONTH_KEY |
| PRESENTED_KEY |
| KURT_ID_OWNER |
| KURT_ID_PAYER |
| KURT_ID_USER |
| CUST_HOUSEHOLD_ID |
| CUST_FAR_ID |
| CUST_AGE |
| CELL_PACKAGE_SK |
| CUST_AGE_GROUP_KEY |
| GENDER |
| IS_SUBS_CAMP |
| SUBSCRIPTION_KEY |
| MAIN_NUMBER |
| CONTACT_PRODUCT_KEY |
| CONTACTED_BIND_START_DATE_KEY |
| CONTACTED_BIND_END_DATE_KEY |
| PROFIT_ID |
| CUST_STRATEGIC_SEGMENT_KEY |
| CUST_SEGMENT_KEY |
| SUBSCRIPTION_SEGMENT_KEY |
| RESPONSE_DATE_KEY |
| RESPONSE_KEY |
| RESPONSE_CHANNEL_KEY |
| RESPONSE_REASON_KEY |
| SUBS_DATA_GROUP_KEY |
| SUBS_TRAFFIC_GROUP_KEY |
| ORDER_ID |
| ORDER_SERVICE_PROVIDER_KEY |
| ORDER_DEALER_KEY |
| ORDER_MATCH_KEY |
| ORDER_LINE_TYPE_KEY |
| ORDER_BINDING_PRODUCT_KEY |
| PRESENTED_DURATION_KEY |
| PRESENTED_DATE_KEY |
| TREATMENT_PRODUCT_KEY |
| TREATMENT_HASH_VAL |
| CUST_RESPONSE_KEY |
| CONTACT_TIME_KEY |
| KPI_NEWSALE |
| KPI_PRODUCT_CHANGE |
| ORDER_SOURCE_SYSTEM_KEY |
| ORDER_DT_KEY |
| CAMPAIGN_HIT_TYPE_KEY |
| CONTACT_HANDSET_KEY |
| CONTACT_SECONDS |
| CONTACT_LOCATION |
| ORDER_STATUS_KEY |
| CONTACT_TEAM |
| CHURN_GROUP_KEY |
| ORDER_RANK_GROUP_KEY |
| ORDER_HANDSET_KEY |
| BINDING_BENEFIT_DESC |
| ORDER_DAYS |

- ← [[CRM_ANALYSE.KIM_ORDER_RANK_GROUP_DIM]]
| Column Name |
|---|
| ORDER_RANK_GROUP_KEY |

- ← [[CRM_ANALYSE.KIM_ORDER_MATCH_DIM]]
| Column Name |
|---|
| ORDER_MATCH_KEY |

- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]
| Column Name |
|---|
| RESPONSE_KEY |
| RESPONSE_GROUP |
| RESPONSE_NM |

- ← [[CRM_ANALYSE.KIM_COMMUNICATION_DIM]]
| Column Name |
|---|
| COMMUNICATION_KEY |
| ACTION_CATEGORY |

- ← [[CRM_ANALYSE.KIM_CHURN_GROUP_DIM_V]]
| Column Name |
|---|
| CHURN_GROUP_KEY |
| CHURN_GROUP_NAME |

- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
| Column Name |
|---|
| ID |
| PARENT |
| TYPE |
| SORT_ORDER |


