# ADM_LOAD_HISTORY_CLEANUP_OK

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Updates the 'JOBSTATUS' of a specific load history entry (identified by LOAD_ID) in the ADM_LOAD_HISTORY table to 'ENDED OK OK', signaling a successful completion.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_LOAD_HISTORY]]
| Column Name |
|---|
| LOAD_ID |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_LOAD_HISTORY]]
| Column Name |
|---|
| JOBSTATUS |

