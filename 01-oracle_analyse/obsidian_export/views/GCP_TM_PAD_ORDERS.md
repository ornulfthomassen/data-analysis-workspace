# GCP_TM_PAD_ORDERS

**Schema:** `CCM` | **Type:** `View`

## Description
Consolidates and prepares TeleMarketing (TM) order-related report data, including customer, order, agent, product, and campaign details, for reporting purposes, specifically for SAS Viya. It maps raw customer IDs from order data to standardized customer keys.

## Data Sources (Inputs)
- ← [[PAD_STAGE.PAD_ORDERS]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]

