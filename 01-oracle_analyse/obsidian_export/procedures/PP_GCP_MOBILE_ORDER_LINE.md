# PP_GCP_MOBILE_ORDER_LINE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `PP_GCP_MOBILE_ORDER_LINE`, is designed to incrementally load or refresh monthly mobile order line data into a highly partitioned target table named `GCP_MOBILE_ORDER_LINE`. It achieves this by first creating and populating two temporary dimension staging tables (`TMP_PRODUCT_DIM` and `TMP_MOB_EQUIPMENT_DIM`) from source views. It then iterates through a specified range of months, and for each month, it ensures that the necessary partitions and sub-partitions exist in the `GCP_MOBILE_ORDER_LINE` table. For various sub-partition types ('AO', 'SO', 'FT', 'HW', 'NB'), it calls an external procedure (`CLM_ADM.PP_GCP_TMP_MOBILE_ORDER_LINE`) which is presumed to populate a temporary staging fact table (`TMP_MOBILE_ORDER_LINE`). Finally, it uses an `ALTER TABLE ... EXCHANGE SUBPARTITION` operation to efficiently swap the data from the temporary staging fact table into the corresponding sub-partition of the permanent `GCP_MOBILE_ORDER_LINE` table, optimizing data loading and minimizing downtime.

## Data Sources (Inputs)
- ← [[CCM.VYA_PRODUCT_DIM]]
- ← [[CCM.VYA_MOBILE_EQUIPMENT_DIM]]
- ← [[DUAL]]
- ← [[GALAXY.DATE_DIM_MV]]

## Target Tables (Outputs)
- → [[TMP_PRODUCT_DIM]]
- → [[TMP_MOB_EQUIPMENT_DIM]]

