# V_MAIN_NUMBER_2Y_PORT_HIST

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates and summarizes the mobile number portability history (port-in and port-out events) for each unique owner and main number combination. It specifically focuses on events that occurred within the last two years (730 days) from the current date. For these events, the view calculates the total count of porting operations, the earliest and latest port-in dates, the earliest and latest port-out dates, and provides a concatenated list of service providers involved in both port-in and port-out events.

## Data Sources (Inputs)
- ← [[ADM_MOBIL_SUBSCR_HIST]]

