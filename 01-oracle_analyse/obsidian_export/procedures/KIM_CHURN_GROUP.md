# KIM_CHURN_GROUP

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure identifies churn-related contacts based on various criteria (termination, porting outbound, product flags, contact date range) and updates their churn group key and order days in the KIM_CAMPAIGN_DETAIL_FACT table. It also logs the start and end status of its execution in the CLM_CCM.GOV_DQ_MARTS table.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_MOB_FACT_V]]
| Column Name |
|---|
| resource_value |
| ORDER_DT_KEY |
| ORDERLINE_PRODUCT_KEY |
| KPI_PORTING_OUTBOUND_SPEECH |
| KPI_SUBSCRIPTION_TERMINATION |
| market_area_key |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DATE_KEY |
| DAY |
- ← [[GALAXY.product_dim]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_FAMILY_NAME |
| PRODUCT_NAME |
| PRIMARY_PRODUCT_FLAG |
| DRM_COMMON_REPORTING |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_AREA |
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| MAIN_NUMBER |
| CONTACT_DTTM |
| CHURN_GROUP_KEY |
| CONTACT_KEY |
| KPI_PORTING_OUTBOUND |
| KPI_SUBSCRIPTION_TERMINATION |
- ← [[CLM_CCM.GOV_DQ_MARTS]]
| Column Name |
|---|
| SYSTEM_NM |
| PROCESS_NM |
| STATUS_NM |
| RUNTIME |

## Target Tables (Outputs)
- → [[CLM_CCM.GOV_DQ_MARTS]]
| Column Name |
|---|
| RUNTIME |
| FREQ |
| SYSTEM_NM |
| PROCESS_NM |
| STATUS_NM |
| REASON |
| PRIORITY |
| START_TIME |
| END_TIME |
| PREV_OK_DTTM |
| PREV_OK_RESSULT |
| LAST_RESSULT |
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CHURN_GROUP_KEY |
| ORDER_DAYS |
| CONTACT_KEY |

