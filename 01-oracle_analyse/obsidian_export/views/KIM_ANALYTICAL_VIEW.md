# KIM_ANALYTICAL_VIEW

**Schema:** `CCM` | **Type:** `View`

## Description
This Oracle SQL view, `KIM_ANALYTICAL_VIEW`, serves as a comprehensive analytical data mart for CRM (Customer Relationship Management) campaigns, sales, and customer interactions. It denormalizes data from a central `KIM_CAMPAIGN_DETAIL_FACT` table with numerous dimension tables to provide a wide array of attributes related to customer demographics, campaign details, product information (from, to, binding, contact, and treatment products), sales channels, dealer information, response details, and geographical data. The view calculates various Key Performance Indicators (KPIs) such as sales volume (`KPI_SALES`), terminal sales (`KPI_TERMINAL`), overall success (`KPI_SUCCESS`), presented offers (`KPI_PRESENTED`), accepted offers (`KPI_ACCEPTED`), selected offers (`KPI_SELECTED`), new sales for mobile postpaid products (`KPI_NEWSALE_MPP`), and anti-churn activities (`KPI_ANTICHURN`). It also derives hierarchical groupings for sales matrices, and generates unique monthly keys for customer, household, subscription, and main number. The primary purpose is to enable detailed reporting and analysis of campaign effectiveness, sales performance, customer churn prevention, and product uptake across different dimensions.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
- ← [[CRM_ANALYSE.DATE_DIM_VA]]
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DIM_V]]
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_GROUP_DIM_V]]
- ← [[CRM_ANALYSE.KIM_CHANNEL_DIM_V]]
- ← [[CRM_ANALYSE.KIM_CHURN_GROUP_DIM]]
- ← [[CRM_ANALYSE.KIM_COMMUNICATION_DIM_V]]
- ← [[CRM_ANALYSE.PRODUCT_DIM_VA]]
- ← [[CLM_CCM.CCM_HOUSEHOLD_INFO]]
- ← [[CRM_ANALYSE.DIMPOSTNUMMER_V]]
- ← [[CRM_ANALYSE.DEALER_DIM_VA]]
- ← [[CRM_ANALYSE.DIMPOSTNUMMER_T]]
- ← [[CRM_ANALYSE.HANDSET_DIM_VA]]
- ← [[CRM_ANALYSE.KIM_ORDER_MATCH_DIM_V]]
- ← [[CRM_ANALYSE.KIM_ORDER_RANK_GROUP_DIM_V]]
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM_V]]
- ← [[CRM_ANALYSE.SOURCE_SYSTEM_DIM_VA]]
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM_V]]

