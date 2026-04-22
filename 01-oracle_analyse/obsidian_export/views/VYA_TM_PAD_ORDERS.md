# VYA_TM_PAD_ORDERS

**Schema:** `CCM` | **Type:** `View`

## Description
This view is designed to load PAD (presumably 'Plan And Dial' or similar system) Order data into a Mjøsa system. It consolidates order details, customer information (both primary and main order customer), agent details, campaign data, and other related attributes from various source systems, performing necessary joins and data transformations (e.g., converting agent ID to lowercase, truncating load dates).

## Data Sources (Inputs)
- ← [[PAD_STAGE.PAD_ORDERS]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]

