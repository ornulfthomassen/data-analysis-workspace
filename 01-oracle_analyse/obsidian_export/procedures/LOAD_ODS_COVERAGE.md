# LOAD_ODS_COVERAGE

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `LOAD_ODS_COVERAGE`, is designed to refresh or initially populate a central 'ODS Coverage' data table (`ODS_COVERAGE`) with comprehensive geographical and service availability information. It aggregates detailed coverage attributes, including mobile network quality, fixed broadband access types (fiber, coax, DSL, AE), home status, MDU agreements, and planned activities, from various source systems. The procedure employs a sophisticated 'blue-green' deployment strategy to ensure high availability and data integrity during updates. It creates a temporary staging table (`ODS_COVERAGE_TMP`) for processing new data, builds indexes on it, and then strategically renames tables (`ODS_COVERAGE` to `ODS_COVERAGE_BKP`, and `ODS_COVERAGE_TMP` to `ODS_COVERAGE`) based on table existence and data volume comparison, effectively swapping the active data set with the newly processed data. It also logs the status of these swap operations.

## Data Sources (Inputs)
- ← [[CCDW_CTI.CTI_CONS_HOUSEHOLD]]
- ← [[CCDW.GEOGRAPHY_ATTRIBUTES_FAR]]
- ← [[KAS.SAMBAND_HIST]]
- ← [[KAS.BOLIG_HIST]]
- ← [[KAS.ADRESSE_TILLEGG_HIST]]
- ← [[DUAL]]
- ← [[ALL_TABLES]]
- ← [[USER_INDEXES]]

## Target Tables (Outputs)
- → [[ODS_COVERAGE]]
- → [[ODS_COVERAGE_TMP]]
- → [[ODS_COVERAGE_BKP]]
- → [[CLM_CCM.ODS_PROCEDURE_SWAP_STATUS]]

