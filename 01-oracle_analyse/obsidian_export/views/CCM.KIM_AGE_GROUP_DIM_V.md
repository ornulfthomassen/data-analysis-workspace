# KIM_AGE_GROUP_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a dimensional view for age groups by selecting relevant columns from the ANALYTICAL_GROUP_DIM table. It performs a self-join to filter for age groups based on a hierarchical relationship where the parent entry is specifically identified by 'AGE' in the 'NAME' column.

## Data Sources (Inputs)
- ← [[CCM.ANALYTICAL_GROUP_DIM]]
| Column Name |
|---|
| ID |
| NAME |
| DESCRIPTION |
| VALUE_FROM |
| VALUE_TO |
| H_LEVEL |
| PARENT |
| SORTING |
| TYPE_ID |


