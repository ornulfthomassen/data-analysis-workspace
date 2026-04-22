# VYA_INSIGHT_DEVICE_FROM_TB

**Schema:** `CCM` | **Type:** `View`

## Description
Extracts and consolidates anonymized sales details for devices sold through 'Telenorbutikken' (TBD), enriching the data with hierarchical product group information, customer subscription details, and dealer dimensions. The view is designed to prepare this device-centric sales data for an analytics platform, likely Viya, by handling potential duplicates and ensuring a single, comprehensive record per unique device (identified by IMEI/serial number) via aggregation and ranking.

## Data Sources (Inputs)
- ← [[THIRD_PARTY_SERVICES.MATERIAL_GROUPS_STAGE]]
- ← [[THIRD_PARTY_SERVICES.T_BUTIKKEN_DEVICES]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[GALAXY.DEALER_DIM]]

