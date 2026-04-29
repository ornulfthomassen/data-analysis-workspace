# P_ADM_ROLLOVER

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Manages historical data rollover for the `ADM_ROLLOVER` table. It processes data for a specific month (`P_YYYYMM`), dynamically creating a new partition or verifying an existing one within `CLM_ADM.ADM_ROLLOVER`. It populates a temporary table (`CLM_ADM.TMP_ROLLOVER`) with aggregated and joined data from various source tables. Finally, it uses an `EXCHANGE PARTITION` operation to load the data from the temporary table into the `CLM_ADM.ADM_ROLLOVER` table's corresponding monthly partition.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
| SUBOBJECT_NAME |
- ← [[CLM_ADM.ADM_ROLLOVER]]
- ← [[CRM_ANALYSE.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| LAST_DATE |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |
- ← [[CM.SUBSCRIPTION_OFFER_INCENTIVE]]
| Column Name |
|---|
| PRODUCT_OFFER_ID |
| SUBSCR_ID |
| SUBSCRIBED_COMPONENT_ID |
| INFO_IS_DELETED |
| INC_VALID_FROM_DATE |
| INC_VALID_TO_DATE |
- ← [[P_FROM_TABLE]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| LOAD_DATE |
| TP_SUB_KEY |
| SUB_IDENTITY |
| INIT_BALANCE |
| O_ID |
| PURCHASE_SEQ |
- ← [[CLM_CCM.ROLLOVER]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| LOAD_DATE |
| SUBSCR_ID |
| MAIN_NUMBER |
| INIT_BALANCE_MB |
| INIT_BALANCE |
| O_ID |
| PURCHASE_SEQ |

## Target Tables (Outputs)
- → [[CLM_ADM.TMP_ROLLOVER]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| LOAD_DATE |
| SUBSCRIPTION_ID |
| SUBSCR_ID |
| MAIN_NUMBER |
| POID |
| INIT_BALANCE_MB |
| INIT_BALANCE |
| O_ID |
| PURCHASE_SEQ |
- → [[CLM_ADM.ADM_ROLLOVER]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| LOAD_DATE |
| SUBSCRIPTION_ID |
| SUBSCR_ID |
| MAIN_NUMBER |
| POID |
| INIT_BALANCE_MB |
| INIT_BALANCE |
| O_ID |
| PURCHASE_SEQ |

