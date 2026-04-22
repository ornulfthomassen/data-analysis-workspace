# VYA_AGREEMENT_DEVICE_PROFIT

**Schema:** `CCM` | **Type:** `View`

## Description
This view calculates and consolidates detailed financial and operational metrics related to device agreements, specifically distinguishing between 'swap' agreements and 'device insurance' agreements. It derives profit-related values (gross, net, VAT, duration) and cost of goods sold (COGS) by leveraging existing agreement data and applying a hierarchical imputation logic for COGS when direct values are missing. The purpose is to provide a comprehensive dataset for analyzing the profitability and performance of different types of device agreements.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_AGREEMENT_DEVICE_PROFIT]]
- ← [[CCM.VYA_AGREEMENT_DEVICE_ALL]]

