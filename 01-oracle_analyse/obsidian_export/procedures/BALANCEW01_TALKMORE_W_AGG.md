# BALANCEW01_TALKMORE_W_AGG

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure aggregates weekly subscription balance data for 'Talkmore' branded products. It dynamically manages a partitioned historical table named `BALANCE_TALKMORE_WEEK_AGG`. For a specified or calculated range of weeks, it checks if the target table exists, creating it if necessary. It then iterates through each week, dropping and re-creating the corresponding partition, and finally inserts aggregated subscription balance (distinct directory numbers) for that week into the new partition. Statistics are gathered on the table/partitions after creation and inserts.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
- ← [[DUAL]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CM.SUBSCRIPTION]]
- ← [[CM.PROD_SERV_MAPPING]]

## Target Tables (Outputs)
- → [[BALANCE_TALKMORE_WEEK_AGG]]

