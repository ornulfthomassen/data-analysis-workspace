# P_ADR_ODS_FAR

**Schema:** `CCM` | **Type:** `Procedure`

## Description
The procedure performs a full data refresh for the `ODS_FAR` table. It populates a temporary table (`ODS_FAR_N`) with data extracted from multiple source systems, then uses a 'table swap' mechanism to replace the current `ODS_FAR` table with the newly loaded data. The existing `ODS_FAR` table is renamed to `ODS_FAR_O` to serve as a backup for the previous state. This swap process is conditional, incorporating checks for table existence, data volume deviation (controlled by `V_RANGE_SWAP`), and index consistency to ensure a safe and controlled refresh. It also handles initial setup (creating `ODS_FAR` if it doesn't exist) and robust error logging via `CLM_CCM.ODS_PROCEDURE_SWAP_STATUS` and `CLM_CCM.P_CCM_LOAD_HISTORY` for monitoring.

## Data Sources (Inputs)
- ← [[GALAXY.LOCATION_DIM]]
- ← [[CCDW.GEOGRAPHY_ATTRIBUTES_FAR]]
- ← [[CCDW.COUNTRY]]
- ← [[CCDW.ADDRESS_TYPE]]
- ← [[CCDW.ADDRESS_STATUS]]
- ← [[CCDW_CTI.CTI_CONS_HOUSEHOLD]]
- ← [[KAS.BOLIG]]
- ← [[KAS.ADRESSER]]
- ← [[VULA.LOAD_VULA_WEB]]

## Target Tables (Outputs)
- → [[ODS_FAR]]
- → [[ODS_FAR_N]]
- → [[ODS_FAR_O]]
- → [[ODS_FAR_O_TEMP]]
- → [[CLM_CCM.ODS_PROCEDURE_SWAP_STATUS]]
- → [[CLM_CCM.CCM_LOAD_HISTORY]]

