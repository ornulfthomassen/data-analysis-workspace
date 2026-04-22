# ADM_AGREEMENTS_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Consolidates and categorizes agreement details, specifically for 'Swap Agreements' and 'Insurance' related to mobile terminals. It extracts product information, device (IMEI) details, associated subscription IDs, and invoice accounts, along with agreement and IMEI status and date ranges.

## Data Sources (Inputs)
- ← [[CCDW.AGREEMENT]]
- ← [[CCDW.AGREEMENT_PRODUCT_CONFIG]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[AGR.EQUIPMENT]]
- ← [[GALAXY.HANDSET_DIM_V]]

