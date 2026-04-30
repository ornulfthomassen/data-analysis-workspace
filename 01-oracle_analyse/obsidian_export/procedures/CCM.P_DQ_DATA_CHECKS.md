# P_DQ_DATA_CHECKS

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Orchestrates and executes data quality check SQL statements, retrieving them dynamically from a configuration table. The specific data sources and target tables for the *dynamically executed* SQL statements cannot be determined from this procedure script alone, as their content is stored as strings in a configuration table.

## Data Sources (Inputs)
- ← [[CLM_CCM.DQ_DATA_CHECKS_ENCODER]]
| Column Name |
|---|
| MEASURE_SQL |
| CHECK_FREQUENCY |
| CURRENT_VERSION |


