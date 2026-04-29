# KIM_CHURN_GROUP_CLM

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Calculates churn group keys and termination days for specific customer contacts based on order line details, product information, and campaign contact data. It then updates the `CHURN_GROUP_KEY` and `ORDER_DAYS` columns in the `KIM_CAMPAIGN_DETAIL_FACT` table for matching contacts. The procedure also logs its execution status (start and completion) into the `CLM_CCM.GOV_DQ_MARTS` table.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_MOB_FACT_V]]
| Column Name |
|---|
| CONTACT_KEY |
| ORDER_DT_KEY |
| resource_value |
| KPI_PORTING_OUTBOUND |
| KPI_SUBSCRIPTION_TERMINATION |
| KPI_PORTING_OUTBOUND_SPEECH |
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
| CONTACT_DTTM |
| MAIN_NUMBER |
| CHURN_GROUP_KEY |
| CONTACT_KEY |

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

