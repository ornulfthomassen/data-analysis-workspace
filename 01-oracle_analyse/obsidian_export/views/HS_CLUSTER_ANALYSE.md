# HS_CLUSTER_ANALYSE

**Schema:** `CCM` | **Type:** `View`

## Description
This view is designed to prepare a unique dataset for cluster analysis. It combines subscription master data with customer segmentation, product information, and usage metrics (like active days, product days, average and standard deviation of MB usage over the last 12 months). The data is filtered to represent a snapshot for a specific historical date (April 30, 2019), likely for analytical processing or reporting.

## Data Sources (Inputs)
- ← [[crm_analyse.hs_fleksi_clusteranal_1904]]
- ← [[clm_adm.adm_subscription_master_hist]]

