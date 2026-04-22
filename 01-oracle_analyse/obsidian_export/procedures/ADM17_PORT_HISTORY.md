# ADM17_PORT_HISTORY

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `ADM17_PORT_HISTORY`, is designed to create and maintain a historical summary table for phone number porting events. It first checks for the existence of the target table, `CRM_ANALYSE.ADM_PORT_HISTORY`. If the table does not exist, it creates it as a partitioned table, sets it to NOLOGGING, and creates an index. The procedure then iterates through a range of months (determined by input parameters or derived from the current date), ensuring that a corresponding partition exists for each month in the target table. For each month, it calculates and inserts aggregated porting data (such as main number, count of Telenor ports, total ports, shopper flag, first/last port dates, and service provider details) into the `ADM_PORT_HISTORY` table. The data is derived from various source tables, primarily `NRPORT.NRPORT_PORTERINGER`. It also handles error logging and gathers statistics for the created table and its partitions.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
- ← [[DUAL]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY]]
- ← [[NRPORT.NRPORT_PORTERINGER]]

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_PORT_HISTORY]]

