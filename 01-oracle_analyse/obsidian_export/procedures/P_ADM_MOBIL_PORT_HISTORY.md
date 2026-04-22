# P_ADM_MOBIL_PORT_HISTORY

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Processes mobile number porting event history for a specified month. It gathers raw porting data and subscription information, aggregates it into monthly statistics per subscription (including number of ports, first/last port dates, and service providers involved in porting), and then uses a temporary staging table to load this aggregated data into a specific monthly partition of a permanent history table. The procedure includes checks for source data availability and handles existing partitions, either overwriting or creating new ones.

## Data Sources (Inputs)
- ← [[NRPORT.NRPORT_PORTERINGER]]
- ← [[ADM_MOB_SUBSCRIPTION_CORE]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]

## Target Tables (Outputs)
- → [[ADM_MOBIL_PORT_HISTORY]]
- → [[TMP_MOBIL_PORT_HISTORY]]

