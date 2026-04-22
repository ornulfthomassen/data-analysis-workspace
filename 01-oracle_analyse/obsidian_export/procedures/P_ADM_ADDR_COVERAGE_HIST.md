# P_ADM_ADDR_COVERAGE_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure processes address coverage data for the previous month. It creates a temporary staging table, populates it with detailed coverage information from a source ODS (Operational Data Store) table, and then loads this data into a specific monthly partition of a permanent, partitioned administrative table. It handles the creation of new partitions if they don't exist and includes logic to prevent overwriting existing data for a partition unless explicitly allowed.

## Data Sources (Inputs)
- ← [[CLM_CCM.ODS_COVERAGE]]

## Target Tables (Outputs)
- → [[TMP_ADDR_COVERAGE_HIST]]
- → [[ADM_ADDR_COVERAGE_HIST]]

