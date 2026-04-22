# P_ADR_ODS_COVERAGE

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This Oracle PL/SQL procedure, P_ADR_ODS_COVERAGE, is designed to refresh a master coverage data table (ODS_COVERAGE) using a temporary table-swap mechanism. It gathers detailed address and service coverage information from various source systems, constructs a new dataset in a temporary table (ODS_COVERAGE_N), creates necessary indexes, and then performs a 'hot swap' operation. The 'hot swap' involves renaming the existing ODS_COVERAGE table to ODS_COVERAGE_O (backup) and renaming ODS_COVERAGE_N to ODS_COVERAGE, ensuring minimal downtime. The procedure includes logic to handle initial loads (when ODS_COVERAGE doesn't exist or is empty), manage index renaming, and includes a configurable threshold (V_RANGE_SWAP) to prevent unintended data loss or significant changes by stopping the swap if the row count difference between the old and new data exceeds the threshold. It also logs execution status and errors to dedicated logging tables.

## Data Sources (Inputs)
- ← [[CCDW_CTI.CTI_CONS_HOUSEHOLD]]
- ← [[CCDW.GEOGRAPHY_ATTRIBUTES_FAR]]
- ← [[KAS.SAMBAND_HIST]]
- ← [[KAS.BOLIG_HIST]]
- ← [[KAS.ADRESSE_TILLEGG_HIST]]

## Target Tables (Outputs)
- → [[ODS_COVERAGE]]
- → [[ODS_COVERAGE_N]]
- → [[ODS_COVERAGE_O]]
- → [[ODS_COVERAGE_O_TEMP]]
- → [[CLM_CCM.ODS_PROCEDURE_SWAP_STATUS]]
- → [[CLM_CCM.CCM_LOAD_HISTORY]]

