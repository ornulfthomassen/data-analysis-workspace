# SOURCE_SYSTEM_DIM_VA

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a dimension view for source systems, standardizing the 'source_system_name' and 'source_system_desc' columns. It handles null values by replacing them with '-1' (casted to string) and enforces specific VARCHAR2 lengths for these columns, while retaining the 'source_system_KEY'. This view likely serves as a cleaned or formatted representation of source system metadata.

## Data Sources (Inputs)
- ← [[galaxy.source_system_dim_v]]

