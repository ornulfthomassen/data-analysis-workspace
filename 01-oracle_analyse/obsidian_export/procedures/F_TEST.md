# F_TEST

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This procedure first implements a waiting mechanism, repeatedly checking a data readiness flag (`DATA_IS_FRESH`) from the `V_WAIT_FOR_DATA` view until the data is deemed ready or a 30-second timeout occurs. If the data becomes ready within the timeout, it then manages a temporary table named `TABLE_FROM_PROC_IN_WITH`. It dynamically drops this temporary table if it already exists, and subsequently recreates it by selecting a small sample (first 5 rows) of device keys and cast source device IDs from the `GALAXY.DEVICE_DIM` table.

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

