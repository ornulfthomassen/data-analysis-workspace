# GCP_PRODUCT_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
Consolidates and enriches product dimension data from multiple source systems, providing a comprehensive set of product attributes including general information, reporting classifications, pricing details (fees, included services, and after-inclusion prices), and business/consumer segmentation flags. It includes specific logic for classifying products from various sources, particularly for 'Talkmore' offerings, and derives certain attributes like included data volume from product names. This view serves as a unified product dimension for analytical and reporting purposes within the CCM (Customer Communication Management) domain.

## Data Sources (Inputs)
- ← [[PD]]
- ← [[CLM_ADM.TALKMORE_PRIM_PRODUCT_DIM]]

