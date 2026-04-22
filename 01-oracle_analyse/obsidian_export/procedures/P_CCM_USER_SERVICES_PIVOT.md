# P_CCM_USER_SERVICES_PIVOT

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure (`P_CCM_USER_SERVICES_PIVOT`) aggregates and pivots user activity data for various OTT (Over-The-Top) services and Minsky (cloud storage) usage at a customer level. It constructs a new version of the pivoted data into a staging table (`CCM_USER_SERVICES_PIVOT_N`), applies indexes and grants, then performs a "hot swap" operation. In this swap, the existing `CCM_USER_SERVICES_PIVOT` table is renamed to a backup table (`CCM_USER_SERVICES_PIVOT_O`), and the newly built staging table (`CCM_USER_SERVICES_PIVOT_N`) is renamed to become the new `CCM_USER_SERVICES_PIVOT`. The old backup table (`CCM_USER_SERVICES_PIVOT_O`) is subsequently dropped. The swap is conditional, proceeding only if the row count deviation between the new data and the existing data is within a defined threshold, unless a force-swap option is used.

## Data Sources (Inputs)
- ← [[CCDW_USAGE.OTT_SERVICES_USAGE_AGG]]
- ← [[CCDW_USAGE.OTT_SERVICES]]
- ← [[ODS.CONNECT_ID_LINK]]
- ← [[CLM_CCM.CCM_CUST_CHANNEL_INTERACTION]]
- ← [[COMOYO.MINSKY_MAIN_DAILY]]
- ← [[CLM_CCM.CCM_USER_SERVICES_PIVOT]]

## Target Tables (Outputs)
- → [[CCM_USER_SERVICES_PIVOT_N]]
- → [[CCM_USER_SERVICES_PIVOT_O]]
- → [[CCM_USER_SERVICES_PIVOT]]

