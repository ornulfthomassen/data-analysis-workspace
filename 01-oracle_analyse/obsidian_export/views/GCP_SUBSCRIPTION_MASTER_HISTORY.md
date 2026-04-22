# GCP_SUBSCRIPTION_MASTER_HISTORY

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a historical view of subscription master data, tracking changes in key attributes such as ownership, market area, product configuration, and start/end dates. It exposes current values, previous values, and original values for various subscription characteristics, and calculates specific flags (e.g., USER_BECAME_OWNER_FLAG) based on these changes to identify lifecycle events like ownership transfers.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]

