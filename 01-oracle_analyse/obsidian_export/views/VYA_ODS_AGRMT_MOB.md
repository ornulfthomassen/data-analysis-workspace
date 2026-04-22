# VYA_ODS_AGRMT_MOB

**Schema:** `CCM` | **Type:** `View`

## Description
Prepares and consolidates core mobile agreement data, including customer and device details, from an Operational Data Store (ODS) layer for loading into a data warehouse or another data system (referred to as Mjøsa). It derives customer identifiers and device keys by joining agreement data with customer mapping information.

## Data Sources (Inputs)
- ← [[CLM_CCM.V_ODS_AGRMT_MOB]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]

