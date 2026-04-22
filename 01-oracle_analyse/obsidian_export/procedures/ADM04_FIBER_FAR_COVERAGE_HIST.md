# ADM04_FIBER_FAR_COVERAGE_HIST

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure extracts fiber coverage data from the `FAR.FIBER_FAR_COVERAGE` table for a specific month (`V_YYYYMM`), stages this data into a temporary table named `TMP_FIBER_FAR_COVERAGE_HIST`. After creating and populating the temporary table, it then moves this data into a monthly partition of a permanent historical table, `ADM_FIBER_FAR_COVERAGE_HIST`, using an `ALTER TABLE ... EXCHANGE PARTITION` operation. It handles the dropping and recreation of the temporary table and the creation of the target partition if it doesn't already exist.

## Data Sources (Inputs)
- ← [[FAR.FIBER_FAR_COVERAGE]]

## Target Tables (Outputs)
- → [[TMP_FIBER_FAR_COVERAGE_HIST]]
- → [[ADM_FIBER_FAR_COVERAGE_HIST]]

