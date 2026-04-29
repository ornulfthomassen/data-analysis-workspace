# BALANCE01_MOBILE_SEGMENT_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Creates and populates a partitioned historical table (`BALANCE_MOBILE_SEGMENT_HIST`) with mobile subscription segment data. It iterates through a specified range of months, consolidating information from various operational and analytical sources such as subscription details, product dimensions, porting events, and profit/churn/VAR segments. The procedure uses temporary staging tables (`NRPORT_PORTERINGER_M_MV`, `SUBSCRIPTION_BALANCE_RAW_M_MV`) for intermediate data processing and dynamically manages table partitions for the main historical table.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
| SUBOBJECT_NAME |
- ← [[DUAL]]
| Column Name |
|---|
| SYSDATE |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
| DATE_KEY |
- ← [[NRPORT.NRPORT_PORTERINGER]]
| Column Name |
|---|
| PORT_LOG_VALID_FROM_DATE |
| MSISDN_ID |
| SUBSCR_ID |
| SERVICE_PROVIDER_ID_PORT_FROM |
| SERVICE_PROVIDER_ID_PORT_TO |
- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| PRODUCT_OFFER_ID |
| MARKET_AREA_ID |
| BUSINESS_AREA_ID |
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| END_DATE |
| BINDING_START_DATE |
| START_DATE |
- ← [[GALAXY.PRIMARY_PRODUCT_DIM_V]]
| Column Name |
|---|
| PRIM_PRODUCT_KEY |
| DRM_COMMON_PRODUCT_AREA |
| PRIM_PRODUCT_DESC |
| DRM_COMMON_PAYMENT |
| DRM_COMMON_BRAND |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SOURCE_SYSTEM_ID |
- ← [[PROFIT.CP_CAT_PRIV]]
| Column Name |
|---|
| PERIOD_ID |
| CATEGORY |
| SUBSCRIPTION_ID |
- ← [[crm_analyse.PROFITSEGMENT_MOBILE]]
| Column Name |
|---|
| END_DATE |
| SUBSCRIPTION_ID |
| START_DATE |
| SEGMENT_ID |
- ← [[crm_analyse.VARSEGMENT_MOBILE]]
| Column Name |
|---|
| END_DATE |
| SUBSCRIPTION_ID |
| START_DATE |
| SEGMENT_ID |
- ← [[crm_analyse.CHURNSEGMENT_MOBILE]]
| Column Name |
|---|
| END_DATE |
| SUBSCRIPTION_ID |
| START_DATE |
| SEGMENT_ID |
- ← [[ADM_MOBIL_SUBSCR_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SUBSCR_ID |
| ORIGINAL_START_DATE |
| OWNER |
| ORIGINAL_START_DATE_ORIG |
- ← [[CCDW_SEGMENT.CUSTOMER_SEGMENT]]
| Column Name |
|---|
| KURT_ID |
| MODEL_ID |
| START_DATE |
| END_DATE |
| SEGMENT_ID |

## Target Tables (Outputs)
- → [[CLM_ADM.BALANCE_MOBILE_SEGMENT_HIST]]
| Column Name |
|---|
| REFRESH_DATE |
| PERIOD_MONTH_KEY |
| YEAR_MONTH |
| LAST_DATE |
| PRIM_PRODUCT_DESC |
| DRM_COMMON_PAYMENT |
| DRM_COMMON_BRAND |
| BINDINGSSTATUS |
| BINDINGSUTLOP |
| PROFIT_CAT |
| PROFIT_PERIOD |
| VAR_SEGMENT |
| CHURN_SEGMENT |
| SUBSCRIPTION_KEY |
| MAIN_NUMBER |
| SUBSCR_ID |
| PORT_MAIN_NUMBER |
| PORT_SUBSCR_ID |
| IN_PORT_SP_ID |
| OUT_PORT_SP_ID |
| CLM_LIVSFASE_SEGMENT_ID |
| MAP2_SEGMENT_ID |
| SUBS_START_MONTH_KEY |
| MNO_START_MONTH_KEY |
- → [[CLM_ADM.NRPORT_PORTERINGER_M_MV]]
| Column Name |
|---|
| PORT_YEAR_MONTH_NUMBER |
| PORT_MAIN_NUMBER |
| PORT_SUBSCR_ID |
| IN_PORT_SP_ID |
| OUT_PORT_SP_ID |
- → [[CLM_ADM.SUBSCRIPTION_BALANCE_RAW_M_MV]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| PRIM_PRODUCT_DESC |
| DRM_COMMON_PAYMENT |
| DRM_COMMON_BRAND |
| BINDING_START_DATE |
| BINDINGSUTLOP |
| LAST_DATE |

