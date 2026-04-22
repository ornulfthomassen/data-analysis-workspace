# BMGM_PRODUCT_DIM

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view, "BMGM_PRODUCT_DIM", consolidates and categorizes product information from a central product dimension table (GALAXY.PRODUCT_DIM). It enriches the product data by deriving specific business metrics and roles ('USER' or 'OWNER') based on the product's source system ('Pacman', 'deFakto', 'KAS'), product area, category, paytype, and reporting type. The view calculates flags for various product ownership/usage types such as private postpaid subscriptions, swap agreements, business postpaid usage, mobile broadband, fixed broadband, and fixed telephony subscriptions.

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]

