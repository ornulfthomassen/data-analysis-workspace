# DEALER_DIM_VA

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `DEALER_DIM_VA`, provides a comprehensive and standardized set of dealer-related attributes. Its primary function is to serve as a dealer dimension for analytical purposes within the `CRM_ANALYSE` schema. It performs data cleansing by replacing null values with '-1' (as a string) and casting various fields to specific VARCHAR2 lengths. A key functionality is the derivation of a 'SALES_CHANNEL' classification based on `DRM_SALES_CHANNEL_GEN04_DESC` or `DEALER_CHAIN_NAME`, categorizing dealers into 'Ekstern retail' (External retail), 'Telenorbutikken' (Telenor Store), or using existing descriptions.

## Data Sources (Inputs)
- ← [[GALAXY.DEALER_DIM]]

