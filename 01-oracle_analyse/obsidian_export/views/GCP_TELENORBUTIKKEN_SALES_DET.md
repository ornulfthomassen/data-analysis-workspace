# GCP_TELENORBUTIKKEN_SALES_DET

**Schema:** `CCM` | **Type:** `View`

## Description
This view, GCP_TELENORBUTIKKEN_SALES_DET, is designed to extract, anonymize, and enrich detailed sales transaction data from Telenorbutikken for loading into Google Cloud Platform (GCP). It combines raw sales information with dealer details, hierarchical product group categories (up to three levels), and subscription history for both sales clerks and customers. The view calculates adjusted financial metrics (e.g., net value, quantity) by considering invoice types for returns or adjustments, and anonymizes customer and seller names. It also includes filtering to retrieve data from the current year and the two preceding years based on the invoice date.

## Data Sources (Inputs)
- ← [[THIRD_PARTY_SERVICES.T_BUTIKKEN_DEVICES]]
- ← [[THIRD_PARTY_SERVICES.MATERIAL_GROUPS_STAGE]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]

