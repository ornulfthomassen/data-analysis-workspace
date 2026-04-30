# KIM_LASR_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides an aggregated and comprehensive analytical dataset for Customer Relationship Management (CRM) or marketing campaign performance. It combines key performance indicators (KPIs) and volume metrics from a central fact table (`KIM_LASR_FACT_AGG`) with detailed descriptive attributes from numerous dimension tables related to campaigns, dates, channels, treatments, churn groups, products, responses, handsets, and dealers. The view is filtered to include data from January 1, 2019, onwards and only records with a valid response key, likely for recent and meaningful analytical insights.

## Data Sources (Inputs)
- ← [[CLM_KIM.KIM_LASR_FACT_AGG]]
| Column Name |
|---|
| _KPI_ACCEPTED_Sum_ |
| _KPI_ALL_SALES_Sum_ |
| _KPI_PRESENTED_Sum_ |
| _KPI_SALES_Sum_ |
| _KPI_SELECTED_Sum_ |
| _VOLUME_Sum_ |
| _CONTACT_DTTM_Max_ |
| ACTIVITY_DESC |
| ACTIVITY_ID |
| ACTIVITY_MAIN_OBJECTIVE |
| ACTIVITY_NAME |
| ACTIVITY_OBJECTIVE |
| CAMPAIGN |
| CAMPAIGN_DESC |
| CAMPAIGN_SYSTEM |
| CHURN_GROUP_KEY |
| COMMUNICATION_KEY |
| CONTACT_DATE_KEY |
| CONTACT_HANDSET_KEY |
| CONTACT_PRODUCT_KEY |
| DIALOG_ID |
| DIALOGUE_ID |
| EFFECT_STATUS |
| EFFECT_TYPE |
| ORDER_DEALER_KEY |
| ORDER_FROM_PRODUCT_KEY |
| ORDER_TO_PRODUCT_KEY |
| PROGRAM |
| RESPONSE_DATE |
| RESPONSE_DATE_KEY |
| ROLLE |
| SALES_MATRIX |
| SALES_MATRIX_GROUP |
| SWAP_MATCH |
| TREAT_SWAP_TERMINAL |
| TRIGGER_ID |
| RES_APP_NAME |
| NR_CHURN_SERV_PROV_NM |
| NR_CHURN_SERV_PROV_GR |
| NR_CHURN_CATEGORY_NAME |
| FROM_SERVICE_PROVIDER_GROUP |
| DLR_DRM_SALES_CHANNEL_GEN04 |
| KPI_EFFECT_30D |
| KPI_RESERVATION_30D |
| KPI_NS_OD_CHURN_70D |
| NS_OD_CHURN_CAT |
| KPI_NS_OSD_CHURN_70D |
| NS_OSD_CHURN_CAT |
| KPI_NS_CALL_5D |
| NS_CALL_DAYS_CAT |
| CAMP_CALL_DAYS_CAT |
| KPI_CAMP_CALL_5D |
| CAMPAIGN_KEY |
| channel_key |
| treatment_key |
| source_system_key |
| response_key |
| TREATMENT_product_key |

- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DIM]]
| Column Name |
|---|
| CAMPAIGN_CD |
| CAMPAIGN_NM |
| CAMPAIGN_TYPE_DESC |
| CAMPAIGN_MANAGER |
| CAMPAIGN_KEY |

- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| day |
| year_week_number |
| YEAR_MONTH_NUMBER |
| MONTH_NAME |
| YEAR |
| RELATIVE_WEEK |
| DATE_KEY |

- ← [[CRM_ANALYSE.KIM_CHANNEL_DIM]]
| Column Name |
|---|
| CHANNEL_COMMON_NM |
| channel_key |

- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]
| Column Name |
|---|
| treatment_cd |
| treatment_nm |
| treatment_key |

- ← [[CRM_ANALYSE.KIM_CHURN_GROUP_DIM]]
| Column Name |
|---|
| CHURN_GROUP_DESCRIPTION |
| CHURN_GROUP_NAME |
| churn_group_key |

- ← [[CRM_ANALYSE.KIM_SOURCE_SYSTEM_DIM_V]]
| Column Name |
|---|
| source_system_key |

- ← [[CRM_ANALYSE.PRODUCT_DIM_VA]]
| Column Name |
|---|
| PRODUCT_KEY |
| product_family_name |
| product_name |
| monthly_price |

- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]
| Column Name |
|---|
| response_group |
| response_nm |
| response_key |

- ← [[CRM_ANALYSE.HANDSET_DIM_VA]]
| Column Name |
|---|
| MANUFACTURER |
| MARKETING_NAME |
| HANDSET_KEY |

- ← [[CRM_ANALYSE.KIM_DEALER_DIM_V]]
| Column Name |
|---|
| DRM_SALES_CHANNEL_GEN02_DESC |
| DRM_SALES_CHANNEL_GEN04_DESC |
| DRM_SALES_CHANNEL_GEN07_DESC |
| DEALER_KEY |


