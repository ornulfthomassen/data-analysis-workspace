# P_ADM_MAPSEGMENT_MOBILE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure updates or creates a specific time-based partition within the `ADM_MAPSEGMENT_MOBILE` table. It first prepares data for a given `P_YYYYMM` (year-month) by querying and joining `CRM_ANALYSE.ADM_MAPSEGMENT_MOBILE` and `CLM_ADM.ADM_CUSTOMER_MAPPING_HIST` into a temporary staging table named `TMP_MAPSEGMENT_MOBILE`. Before creating the temporary table, it checks for and drops any pre-existing temporary table with the same name. It then performs an `ALTER TABLE ... EXCHANGE PARTITION` operation to replace the data in the target partition of `ADM_MAPSEGMENT_MOBILE` with the data from the temporary table. If the target partition does not exist, it is created. Finally, it computes statistics for the newly loaded or updated partition.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MAPSEGMENT_MOBILE]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_HIST]]

## Target Tables (Outputs)
- → [[TMP_MAPSEGMENT_MOBILE]]
- → [[ADM_MAPSEGMENT_MOBILE]]

