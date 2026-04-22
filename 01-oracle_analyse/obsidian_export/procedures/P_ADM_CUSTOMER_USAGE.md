# P_ADM_CUSTOMER_USAGE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `P_ADM_CUSTOMER_USAGE` calculates and updates monthly customer usage statistics. For a given month (`V_YYYYMM`), it first ensures the corresponding partition exists in the target table `ADM_CUSTOMER_USAGE`. It then creates a temporary staging table (`TMP_CUSTOMER_USAGE`), populates it with aggregated data derived from various customer and subscription tables, and finally uses an `ALTER TABLE ... EXCHANGE PARTITION` statement to efficiently replace the data in the target partition of `ADM_CUSTOMER_USAGE` with the newly calculated data from the temporary table. Statistics are then computed for the updated partition.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_CORE]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CRM_ANALYSE.ADM_KURT_OWNER_SUBS_AGG]]
- ← [[CRM_ANALYSE.ADM_KURT_USER_SUBS_AGG]]

## Target Tables (Outputs)
- → [[CLM_ADM.TMP_CUSTOMER_USAGE]]
- → [[CLM_ADM.ADM_CUSTOMER_USAGE]]

