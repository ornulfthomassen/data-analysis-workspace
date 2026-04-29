# ADM50_ANALYTICAL_MASTER_TABLES

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure refreshes a set of analytical master tables (Customer, MPP, MPR, MBB) for a given month (`P_YYYYMM`). It implements a 'swap' strategy: it creates a new version of a master table from its corresponding analytical view, then renames the existing master table to a backup, and promotes the newly created table to the main master table. It also manages the creation and renaming of unique indexes and grants SELECT privileges. The procedure can be run for a specific table or all defined tables.

## Data Sources (Inputs)
- ← [[DUAL]]
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
- ← [[V_ANALYTICAL_MASTER_TABLE_CUST]]
- ← [[V_ANALYTICAL_MASTER_TABLE_MPP]]
- ← [[V_ANALYTICAL_MASTER_TABLE_MPR]]
- ← [[V_ANALYTICAL_MASTER_TABLE_MBB]]

## Target Tables (Outputs)
- → [[ANALYTICAL_MASTER_TABLE_CUST]]
- → [[ANALYTICAL_MASTER_TABLE_CUSTNY]]
- → [[ANALYTICAL_MASTER_TABLE_CUSTBK]]
- → [[ANALYTICAL_MASTER_TABLE_MPP]]
- → [[ANALYTICAL_MASTER_TABLE_MPP_NY]]
- → [[ANALYTICAL_MASTER_TABLE_MPP_BK]]
- → [[ANALYTICAL_MASTER_TABLE_MPR]]
- → [[ANALYTICAL_MASTER_TABLE_MPR_NY]]
- → [[ANALYTICAL_MASTER_TABLE_MPR_BK]]
- → [[ANALYTICAL_MASTER_TABLE_MBB]]
- → [[ANALYTICAL_MASTER_TABLE_MBB_NY]]
- → [[ANALYTICAL_MASTER_TABLE_MBB_BK]]

