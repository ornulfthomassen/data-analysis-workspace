# P_CHURN_INSIGHT_CHURN

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure P_CHURN_INSIGHT_CHURN processes and enriches churn-related data for analytical insights. It first performs an initial check on the availability of churn customer subscription and forecast data. If data is available, it creates a temporary staging table (CLM_ADM.INSIGHT_CHURN_WIDE_TEST) by joining various churn, subscription, product category, and forecast views, calculating several derived fields such as churn month, period category, and days between owner change and churn. Subsequently, if the staging table contains data, it truncates and populates another temporary table (CLM_ADM.TMP_CHURN_INSIGHT_CHURN) by further enriching the data from the staging table with customer agreement details to determine an 'ACTIVATED_SAFE_FLAG'. The overall goal is to prepare a wide, detailed dataset for churn analysis by combining and transforming data from multiple sources.

## Data Sources (Inputs)
- ← [[CLM_ADM.CHURN_CUST_SUBSCR_V]]
- ← [[CLM_ADM.CHURN_FORECAST]]
- ← [[CLM_ADM.CHURN_SUBSCR_USR_TO_OWN_V]]
- ← [[CLM_ADM.CHURN_SUBS_PROD_CAT_V]]
- ← [[GALAXY.HOUSEHOLD_MEMBER_DIM_V]]
- ← [[GALAXY.AGREEMENT_DETAIL_FACT]]

## Target Tables (Outputs)
- → [[CLM_ADM.INSIGHT_CHURN_WIDE_TEST]]
- → [[CLM_ADM.TMP_CHURN_INSIGHT_CHURN]]

