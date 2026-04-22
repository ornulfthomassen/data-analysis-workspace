# P_ADM_CUSTOMER_USE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Calculates and updates monthly customer usage and social network analysis (SNA) metrics. It aggregates detailed customer data for a specified month (`P_YYYYMM`) from various source tables into a temporary staging table. Subsequently, this temporary table is used to replace or populate a corresponding monthly partition within the permanent `ADM_CUSTOMER_USE` table, ensuring the target table contains up-to-date monthly customer usage statistics.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_CORE]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CLM_ADM.ADM_CUSTOMER_DETAIL]]
- ← [[CLM_ADM.ADM_CUSTOMER_USAGE]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_DETAIL_HIST]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_USER_DETAIL_HIST]]
- ← [[CRM_ANALYSE.ADM_MOB_KURT_U_TALE_P_REV_3MO]]
- ← [[SYS.ALL_OBJECTS]]

## Target Tables (Outputs)
- → [[TMP_CUSTOMER_USE]]
- → [[ADM_CUSTOMER_USE]]

