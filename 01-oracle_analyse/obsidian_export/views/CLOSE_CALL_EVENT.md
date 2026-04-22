# CLOSE_CALL_EVENT

**Schema:** `CCM` | **Type:** `View`

## Description
For a specific customer identified by MAIN_NUMBER 41683262, this view identifies, for each of their non-'CALL' events, the chronologically first subsequent 'CALL' event. It then calculates and presents the key, date, and the number of days between the initial non-'CALL' event and this subsequent 'CALL' event. This can be used to analyze response times or follow-up activities after various customer interactions.

## Data Sources (Inputs)
- ← [[CUSTOMER_EVENTS]]

