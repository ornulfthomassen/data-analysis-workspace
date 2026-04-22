# CHECK_PARTITION_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies partitioned tables owned by 'CLM_ADM' that are partitioned using the 'PERIOD_MONTH_KEY' column. For each identified table, it extracts the maximum (latest) 6-character suffix from its subobject (partition) names, assuming this suffix represents a date in 'YYYYMM' format, and filters these to include only those greater than '202511'. Its purpose is to monitor or verify the existence and details of future or recent partitions for specific tables.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
- ← [[SYS.ALL_PART_KEY_COLUMNS]]

