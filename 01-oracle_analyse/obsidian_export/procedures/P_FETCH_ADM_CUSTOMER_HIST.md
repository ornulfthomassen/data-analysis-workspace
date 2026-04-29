# P_FETCH_ADM_CUSTOMER_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure iterates through specified monthly periods (July 2022 to August 2024). For each period, it drops a pre-existing monthly snapshot table (e.g., CLM_ADM.ADM_CUSTOMER_202207) if it exists, and then recreates it by copying all data from the CCM.VYA_ADM_CUSTOMER table where the PERIOD_MONTH_KEY matches the current month.

## Data Sources (Inputs)
- ← [[VYA_ADM_CUSTOMER]]
- ← [[ALL_OBJECTS]]
| Column Name |
|---|
| OWNER |
| OBJECT_NAME |

## Target Tables (Outputs)
- → [[ADM_CUSTOMER_YYYYMM]]

