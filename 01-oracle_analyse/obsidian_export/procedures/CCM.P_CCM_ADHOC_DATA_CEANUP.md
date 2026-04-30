# P_CCM_ADHOC_DATA_CEANUP

**Schema:** `CCM` | **Type:** `Procedure`

## Description
The procedure cleans up ad-hoc data entries from the CLM_CCM.CCM_ADHOC_DATA table and their corresponding control records from ADHOC_CMD.ADHOC_CONTROL_SASCI. Deletions are based on campaigns marked for removal (REMOVE_DATA = 'Y') or campaigns whose end date has already passed (END_DATE < SYSDATE).

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_ADHOC_DATA]]
| Column Name |
|---|
| CAMPAIGN_CODE |

- ← [[ADHOC_CMD.ADHOC_CONTROL_SASCI]]
| Column Name |
|---|
| CAMPAIGN_CODE |
| REMOVE_DATA |
| END_DATE |


## Target Tables (Outputs)
- → [[CLM_CCM.CCM_ADHOC_DATA]]
- → [[ADHOC_CMD.ADHOC_CONTROL_SASCI]]

