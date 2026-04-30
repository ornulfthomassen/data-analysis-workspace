# CLOSE_CALL_EVENT

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies specific non-call events for a hardcoded main number (41683262) and associates each with the earliest subsequent call event (from the 'CALLS' partition) for the same main number. It calculates and returns details about this subsequent call, including its key, date, and the number of days elapsed since the initial non-call event.

## Data Sources (Inputs)
- ← [[CCM.CUSTOMER_EVENTS]]
| Column Name |
|---|
| EVENT_DATE |
| EVENT |
| KEY |
| MAIN_NUMBER |


