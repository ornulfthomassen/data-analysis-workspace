# P_ADM_DEVICE_DIM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure P_ADM_DEVICE_DIM is responsible for creating and maintaining a device dimension table named ADM_DEVICE_DIM within the CLM_ADM schema. It extracts raw device data from GALAXY.HANDSET_DIM_V and enriches it with marketing information from CLM_ADM.ADM_GSMA_MARKETING_NAME_DIM. The core logic involves extensive categorization and transformation to derive various device attributes such as manufacturer (shortened), marketing name, type, category, class, OS information, and local sales start date. The procedure employs a 'drop and rename' strategy: it first creates a staging table (TMP_DEVICE_DIM) with the transformed data, performs a row count validation against the existing ADM_DEVICE_DIM, and then drops the old ADM_DEVICE_DIM table (if it exists and validation passes) before renaming TMP_DEVICE_DIM to ADM_DEVICE_DIM. Finally, it creates a unique index, adds a primary key constraint, computes statistics, and grants SELECT privileges on the newly created dimension table.

## Data Sources (Inputs)
- ← [[GALAXY.HANDSET_DIM_V]]
- ← [[CLM_ADM.ADM_GSMA_MARKETING_NAME_DIM]]

## Target Tables (Outputs)
- → [[CLM_ADM.TMP_DEVICE_DIM]]
- → [[CLM_ADM.ADM_DEVICE_DIM]]

