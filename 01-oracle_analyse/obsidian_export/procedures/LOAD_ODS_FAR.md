# LOAD_ODS_FAR

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `LOAD_ODS_FAR`, implements a 'table swap' mechanism for refreshing data in a main target table (`ODS_FAR`). It loads fresh data from multiple source tables into a temporary staging table (`ODS_FAR_N`). Depending on the existence and content of the main table and its backup (`ODS_FAR_O`), and a configurable data change threshold, it renames the temporary table to become the new main table. The old main table is either moved to a backup table or dropped. This approach ensures high availability of the main data table during the refresh process and maintains a historical backup. It also handles initial creation of the main table if it doesn't exist.

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

