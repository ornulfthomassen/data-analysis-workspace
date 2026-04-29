# SOURCE_SYSTEM_DIM_VA

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a dimensional view for source system information, selecting key, name, and description. It handles potential NULL values for name and description by replacing them with '-1' and casts them to specific VARCHAR2 lengths.

## Data Sources (Inputs)
- ← [[galaxy.source_system_dim_v]]
| Column Name |
|---|
| source_system_KEY |
| source_system_name |
| source_system_desc |

