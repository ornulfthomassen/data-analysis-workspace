# P_CCM_ADHOC_DATA_LOAD

**Schema:** `CCM` | **Type:** `Procedure`

## Description
The `P_CCM_ADHOC_DATA_LOAD` procedure is designed to automate the loading of ad-hoc data from various source tables into a central target table. It uses a control table (`ADHOC_CMD.ADHOC_CONTROL_SASCI`) to manage which ad-hoc tables need processing. Before loading, it performs several validation checks for each ad-hoc source table:
1.  **Concurrency Check:** Ensures no other load process for records marked 'Behandles %' is currently active in the control table.
2.  **Control Table Update:** Marks newly identified ad-hoc tables in the control table with a 'Behandles' status.
3.  **Source Data Validation:** For each identified ad-hoc source table, it verifies that the table is not empty and that it contains only one distinct `CAMPAIGN_CODE`.
4.  **Target Data Validation:** Checks if the `CAMPAIGN_CODE` from the ad-hoc source table already exists in the main target table (`CLM_CCM.CCM_ADHOC_DATA`).
If all validations pass, the procedure inserts data from the ad-hoc source table into `CLM_CCM.CCM_ADHOC_DATA`. Finally, it updates the `ADHOC_CMD.ADHOC_CONTROL_SASCI` control table with the final load status (success or various failure reasons, including row counts and campaign codes) and logs any warnings or errors via `CLM_CCM.P_CCM_LOAD_HISTORY`.

## Data Sources (Inputs)
- ← [[ADHOC_CMD.ADHOC_CONTROL_SASCI]]
- ← [[CLM_CCM.CCM_ADHOC_DATA]]
- ← [[ADHOC_CMD.<table_name_from_ADHOC_CONTROL_SASCI.ADHOC_TABLE>]]
- ← [[DUAL]]

## Target Tables (Outputs)
- → [[ADHOC_CMD.ADHOC_CONTROL_SASCI]]
- → [[CLM_CCM.CCM_ADHOC_DATA]]

