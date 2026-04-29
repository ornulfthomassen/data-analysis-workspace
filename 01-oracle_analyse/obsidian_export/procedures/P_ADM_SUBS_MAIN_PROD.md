# P_ADM_SUBS_MAIN_PROD

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure dynamically drops and recreates a permanent table named 'ADM_SUBS_MAIN_PROD' in the 'CLM_ADM' schema. It populates this table with aggregated subscription product information for a specified month (P_YYYYMM), joining data from several source tables including subscription offers, mappings, and product dimensions. After creation, it analyzes the table and grants SELECT privileges to 'CRM_ANALYSE'.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
| SUBOBJECT_NAME |
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| LAST_DATE |
| PERIOD_MONTH_KEY |
- ← [[CM.SUBSCRIPTION_OFFER_INCENTIVE]]
| Column Name |
|---|
| INC_VALID_FROM_DATE |
| INC_VALID_TO_DATE |
| SUBSCR_OFFER_INC_ID |
| PRODUCT_OFFER_ID |
| INFO_IS_DELETED |
| PARAMETER_ID |
| SUBSCR_ID |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SUBSCR_ID |
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |
| SUBSCRIPTION_ID |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| SOURCE_PRODUCT_ID_1 |
| PRODUCT_KEY |

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_SUBS_MAIN_PROD]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| START_DATE |
| END_DATE |
| POID |
| PRODUCT_KEY |

