# TAB_INDEX_PARALLEL

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Synchronizes the parallel degree and instances settings of all indexes belonging to a specified table with the parallel degree of the table itself. If an index's parallel degree or instances setting differs from the table's, the index is altered to match the table's degree and set instances to 1.

## Data Sources (Inputs)
- ← [[CCM.USER_INDEXES]]
| Column Name |
|---|
| index_name |
| degree |
| instances |
| table_name |

- ← [[CCM.USER_TABLES]]
| Column Name |
|---|
| degree |
| instances |
| table_name |


