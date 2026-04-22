# P_CCM_ADHOC_DATA_CEANUP

**Schema:** `CCM` | **Type:** `Procedure`

## Description
The procedure `P_CCM_ADHOC_DATA_CLEANUP` is designed to perform a cleanup operation on ad-hoc campaign data. It identifies and deletes records from the `CLM_CCM.CCM_ADHOC_DATA` table (referred to as the 'main fact table') that are associated with campaigns marked for removal (`REMOVE_DATA = 'Y'`) or have passed their end date (`END_DATE < SYSDATE`), using criteria from the `ADHOC_CMD.ADHOC_CONTROL_SASCI` table. After cleaning the main data table, it proceeds to clean up the `ADHOC_CMD.ADHOC_CONTROL_SASCI` table itself, removing the control entries that meet the same removal or expiry conditions.

## Data Sources (Inputs)
- ← [[ADHOC_CMD.ADHOC_CONTROL_SASCI]]

## Target Tables (Outputs)
- → [[CLM_CCM.CCM_ADHOC_DATA]]
- → [[ADHOC_CMD.ADHOC_CONTROL_SASCI]]

