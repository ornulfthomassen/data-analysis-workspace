# F_TEST2

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This function waits for a data freshness condition based on a flag from 'V_WAIT_FOR_DATA'. If the condition is met within a timeout, it dynamically creates a permanent table named 'TABLE_FROM_PROC_IN_WITH'. Before creation, it checks if this table already exists and drops it. The new table is populated with `DEVICE_KEY` and a casted `SOURCE_DEVICE_ID` from `GALAXY.DEVICE_DIM`, limited to the first 5 rows.

## Data Sources (Inputs)
- ← [[V_WAIT_FOR_DATA]]
| Column Name |
|---|
| DATA_IS_FRESH |
- ← [[GALAXY.DEVICE_DIM]]
| Column Name |
|---|
| DEVICE_KEY |
| SOURCE_DEVICE_ID |

## Target Tables (Outputs)
- → [[TABLE_FROM_PROC_IN_WITH]]
| Column Name |
|---|
| DEVICE_KEY |
| IMEI_USE |

