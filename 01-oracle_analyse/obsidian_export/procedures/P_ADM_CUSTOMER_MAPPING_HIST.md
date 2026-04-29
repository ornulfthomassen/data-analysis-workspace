# P_ADM_CUSTOMER_MAPPING_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure manages monthly partitions for the ADM_CUSTOMER_MAPPING_HIST table. It checks for the existence of the target table and the specific monthly partition (P_YYYYMM). If the partition does not exist, it creates it. It then populates a temporary table (TMP_CUSTOMER_MAPPING_HIST) with transformed customer mapping data from CCDW.CUSTOMER_MAPPING for the specified month. Finally, it exchanges the temporary table with the target partition in ADM_CUSTOMER_MAPPING_HIST, effectively loading the data. It also drops and recreates unique indexes and gathers statistics on the newly loaded partition.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
- ← [[ADM_CUSTOMER_MAPPING_HIST]]
- ← [[CCDW.CUSTOMER_MAPPING]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |

## Target Tables (Outputs)
- → [[TMP_CUSTOMER_MAPPING_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| KURT_ID |
| KURT_KEY |
| CUSTOMER_SK |
| CUSTOMER_SK_KEY |
- → [[ADM_CUSTOMER_MAPPING_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| KURT_ID |
| KURT_KEY |
| CUSTOMER_SK |
| CUSTOMER_SK_KEY |

