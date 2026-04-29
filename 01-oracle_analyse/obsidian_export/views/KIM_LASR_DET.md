# KIM_LASR_DET

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a comprehensive analytical dataset by combining campaign performance, sales, churn, and customer interaction facts (likely pre-aggregated KPIs) with various descriptive dimensions such as campaign details, date information, channel, treatment, churn groups, product details, handset information, and dealer details. It filters data for contact dates from 20190101 onwards and valid response keys.

## Data Sources (Inputs)
- ← [[CLM_KIM.KIM_LASR_FACT]]
| Column Name |
|---|
| _KPI_ACCEPTED_Sum_ |
| _KPI_ANTICHURN_Sum_ |
| _KPI_CHURN_Sum_ |
| _KPI_NEWSALE_MPP_Sum_ |
| _KPI_PRESENTED_Sum_ |
| _KPI_SALES_Sum_ |
| _KPI_SELECTED_Sum_ |
| _KPI_SUCCESS_Sum_ |
| _VOLUME_Sum_ |
| _KPI_ALL_SALES_Sum_ |
| _KPI_SWAP_Sum_ |
| _CONTACT_DTTM_Max_ |
| CONTACT_DATE_KEY |
| RESPONSE_DATE_KEY |
| RESPONSE_DATE |
| SALES_MATRIX |
| SALES_MATRIX_GROUP |
| PROGRAM |
| CAMPAIGN |
| ACTIVITY_OBJECTIVE |
| ACTIVITY_ID |
| ACTIVITY_NAME |
| CAMPAIGN_DESC |
| TRIGGER_ID |
| DIALOGUE_ID |
| EFFECT_STATUS |
| EFFECT_TYPE |
| KPI_EFFECT_30D |
| TREAT_SWAP_TERMINAL |
| ACTIVITY_MAIN_OBJECTIVE |
| ACTIVITY_DESC |
| SWAP_MATCH |
| CAMPAIGN_SYSTEM |
| DIALOG_ID |
| ROLLE |
| COMM_SHAPE_DESCR |
| RES_APP_NAME |
| RESERVATION_DAYS |
| EFFECT_RANK |
| NR_OD_CHURN_DAYS |
| NR_OSD_CHURN_DAYS |
| CAMP_CALL_DAYS |
| NEWSALE_CALL_DAYS |
| CAMP_CALL5_CHURN70 |
| NS_CALL5_CHURN70 |
| KPI_RESERVATION_30D |
| KPI_NS_OD_CHURN_70D |
| KPI_NS_OD_CHURN_15D |
| NS_OD_CHURN_CAT |
| KPI_NS_OSD_CHURN_70D |
| KPI_NS_OSD_CHURN_15D |
| NS_OSD_CHURN_CAT |
| NR_CHURN_SERV_PROV_NM |
| NR_CHURN_SERV_PROV_GR |
| NR_CHURN_CATEGORY_NAME |
| FROM_SERVICE_PROVIDER_GROUP |
| DLR_DRM_SALES_CHANNEL_GEN04 |
| KPI_NS_CALL_5D |
| NS_CALL_DAYS_CAT |
| CAMP_CALL_DAYS_CAT |
| KPI_CAMP_CALL_5D |
| OWNER_AGE_GROUP |
| USER_AGE_GROUP |
| OWNER_AGE |
| USER_AGE |
| MAIN_NUMBER_SK |
| MAIN_NUMBER |
| SUBSCRIPTION_KEY |
| CUSTOMER_SK_OWNER |
| CUSTOMER_SK_USER |
| CUSTOMER_SK_PAYER |
| CONTACT_KEY |
| NEWSALE_DAYS |
| BANK_ID_DAYS |
| CAMPAIGN_KEY |
| contact_date_key |
| channel_key |
| treatment_key |
| churn_group_key |
| source_system_key |
| CONTACT_PRODUCT_KEY |
| order_from_product_key |
| response_key |
| order_to_product_key |
| TREATMENT_product_key |
| CONTACT_HANDSET_KEY |
| ORDER_DEALER_KEY |
- ← [[crm_analyse.KIM_CAMPAIGN_DIM]]
| Column Name |
|---|
| CAMPAIGN_CD |
| CAMPAIGN_NM |
| CAMPAIGN_TYPE_DESC |
| CAMPAIGN_MANAGER |
| CAMPAIGN_KEY |
- ← [[galaxy.date_dim_mv]]
| Column Name |
|---|
| day |
| year_week_number |
| YEAR_MONTH_NUMBER |
| MONTH_NAME |
| YEAR |
| RELATIVE_WEEK |
| DATE_KEY |
- ← [[crm_analyse.kim_channel_dim]]
| Column Name |
|---|
| CHANNEL_COMMON_NM |
| channel_key |
- ← [[crm_analyse.kim_treatment_dim]]
| Column Name |
|---|
| treatment_cd |
| treatment_nm |
| treatment_key |
- ← [[crm_analyse.kim_churn_group_dim]]
| Column Name |
|---|
| CHURN_GROUP_DESCRIPTION |
| CHURN_GROUP_NAME |
| churn_group_key |
- ← [[CRM_ANALYSE.KIM_SOURCE_SYSTEM_DIM_V]]
| Column Name |
|---|
| source_system_key |
- ← [[crm_analyse.PRODUCT_DIM_VA]]
| Column Name |
|---|
| product_family_name |
| product_name |
| monthly_price |
| PRODUCT_KEY |
- ← [[crm_analyse.kim_response_dim]]
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

