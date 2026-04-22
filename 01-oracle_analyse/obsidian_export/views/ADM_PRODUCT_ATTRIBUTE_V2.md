# ADM_PRODUCT_ATTRIBUTE_V2

**Schema:** `CCM` | **Type:** `View`

## Description
This view, 'ADM_PRODUCT_ATTRIBUTE_V2', serves as a standardized and enriched product attribute dimension for CRM analysis. It consolidates product information from the core product dimension table, enriching it with hierarchical product type data. A key function is the extensive data cleansing and transformation of various product metrics (such as startup fees, monthly fees, included minutes/SMS/MMS/data, data prices, baud rates, and baud reduction quotas) from string formats into standardized numerical values (e.g., all data volumes to MB, all baud rates to MBPS). It applies complex business logic, including case statements for handling different units (KB, MB, GB, KBPS, MBPS), replacing text like 'FRI BRUK' or 'Ubegrenset' with numerical equivalents, and assigning default values based on product family, rank, or primary product flags when raw data is missing or ambiguous. The view also filters out products from a specific source system ('Marius').

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]

