# VA_LOGG_DQ

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Logs Data Quality (DQ) process execution status by managing entries in a governance data quality mart table. It updates existing entries to mark them as 'OLD' or to record completion/error status, or inserts new status entries for ongoing processes.

## Data Sources (Inputs)
- ← [[CLM_CCM.GOV_DQ_MARTS]]
| Column Name |
|---|
| SYSTEM_NM |
| PROCESS_NM |
| FREQ |
| STATUS_NM |

## Target Tables (Outputs)
- → [[CLM_CCM.GOV_DQ_MARTS]]
| Column Name |
|---|
| RUNTIME |
| FREQ |
| SYSTEM_NM |
| PROCESS_NM |
| STATUS_NM |
| REASON |
| PRIORITY |
| START_TIME |
| END_TIME |
| PREV_OK_DTTM |
| PREV_OK_RESSULT |
| LAST_RESSULT |

