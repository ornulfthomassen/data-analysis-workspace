# P_ADM_SUBSCR_TWIN_HIST2

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure processes historical subscription twin data for a given month (P_YYYYMM). It performs a series of data completeness checks from various source systems, dynamically creates a partition in the ADM_SUBSCR_TWIN_HIST2 table for the specified month, and then populates a temporary table (TMP_SUBSCR_TWIN_HIST1_2) with aggregated and transformed subscription-related information. Although a final step to exchange the temporary table data into the permanent partitioned table is commented out, the primary function of the active code is to prepare and store this monthly historical snapshot in a temporary staging table.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_MARKET_PRODUCT |
| PRODUCT_NAME |
| PRODUCT_KEY |
| SOURCE_PRODUCT_ID_1 |
| SOURCE_SYSTEM_NAME |
- ← [[CLM_CCM.CCM_TERMINAL_TAC]]
| Column Name |
|---|
| MODELID |
- ← [[CLM_CCM.CCM_TERMINAL_DETAIL]]
| Column Name |
|---|
| MODELID |
- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| SOURCE_SYSTEM_ID |
| BUSINESS_AREA_ID |
| SUBSCRIPTION_ID |
| PARENT_SUBSCRIPTION_ID |
| MAIN_NUMBER |
| START_DATE |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
- ← [[CCDW.SUBSCRIPTION_HANDSET]]
| Column Name |
|---|
| TERMINAL_USE_FIRST_DATE |
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| FIRST_DATE |
| LAST_DATE |
- ← [[CM.SUBSCRIPTION]]
| Column Name |
|---|
| INFO_IS_DELETED |
| SUBSCR_VALID_TO_DATE |
| SUBSCR_VALID_FROM_DATE |
| SUBSCR_ID |
| DIRECTORY_NUMBER_ID |
- ← [[CM.SUBSCRIBED_COMPONENT]]
| Column Name |
|---|
| SUBSCR_ID |
| INFO_IS_DELETED |
| VALID_TO_DATE |
| VALID_FROM_DATE |
| SUBSCRIBED_COMPONENT_ID |
| COMPONENT_ID |
- ← [[CM.SUBSCRIPTION_OFFER_INCENTIVE]]
| Column Name |
|---|
| SUBSCR_ID |
| SUBSCRIBED_COMPONENT_ID |
| PARAMETER_ID |
| INFO_IS_DELETED |
| INC_VALID_TO_DATE |
| INC_VALID_FROM_DATE |
| SUBSCR_OFFER_INC_ID |
| PRODUCT_OFFER_ID |
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]
| Column Name |
|---|
| SUBSCR_ID |
| SUBSCRIBED_COMPONENT_ID |
| INFO_IS_DELETED |
| VALID_TO_DATE |
| VALID_FROM_DATE |
| PARAMETER_ID |
| PARAMETER_VALUE |
| SUBSCR_OFFER_CONFIG_PROD_ID |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |
| SUBSCRIPTION_ID |

## Target Tables (Outputs)
- → [[ADM_SUBSCR_TWIN_HIST2]]
- → [[TMP_SUBSCR_TWIN_HIST1_2]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| SUBSCR_ID |
| DIRECTORY_NUMBER_ID |
| SUBSCR_VALID_FROM_DATE |
| SUBSCR_VALID_TO_DATE |
| TWIN_SUBS_COMP_ID |
| TWIN_SUB_NUMBER |
| SCOMP_VALID_FROM_DATE |
| SCOMP_VALID_TO_DATE |
| TWIN_CM_SOI_ID |
| SOI_VALID_FROM_DATE |
| SOI_VALID_TO_DATE |
| PARAMETER_ID |
| TWIN_TYPE |
| TWIN_PRODUCT_NAME |
| TWIN_PRODUCT_KEY |
| TWIN_POID |
| SUBSCR_OFFER_CONFIG_PROD_ID |
| SOC_VALID_FROM_DATE |
| SOC_VALID_TO_DATE |

