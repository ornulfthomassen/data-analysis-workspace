# P_ADM_TRIGGER_CHECK

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure P_ADM_TRIGGER_CHECK monitors a specified view (P_TRIGGER_VIEW) for a successful status within a given time frame (P_WAIT_MINUTES). It repeatedly queries the view for the latest 'END_TIME', 'RUN_ERR_CODE', and 'RUN_ERR_MSG'. If 'RUN_ERR_CODE' remains non-zero (indicating an error or ongoing process) after the specified waiting period, it raises an application error, otherwise, it completes successfully. It uses a sleep mechanism between checks.

## Data Sources (Inputs)
- ← [[P_TRIGGER_VIEW]]
| Column Name |
|---|
| END_TIME |
| RUN_ERR_CODE |
| RUN_ERR_MSG |

