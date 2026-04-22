# VYA_ADM_ORDEN_ACTIVATION

**Schema:** `CCM` | **Type:** `View`

## Description
This view calculates and presents key activation metrics for 'ORDEN' (likely orders or services) for each customer. It identifies the latest available historical data for 'ORDEN' activations, determines if an 'ORDEN' has been activated (ORDEN_FLG), its availability date, the first activation date, the number of days waited between availability and activation, and the last foreground time. It then maps these activation details to a customer key.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_ORDEN_ACTIVATION_HIST]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]

