# VYA_AGREEMENT_TELENOR_SPILL

**Schema:** `CCM` | **Type:** `View`

## Description
This view retrieves detailed agreement information for specific products identified by their `AGREEMENT_PRODUCT_KEY` (10896117 and 11046082). It combines product names, customer mapping, agreement offer details, agreement start/end dates, and various product quantities related to these specific agreements. The 'TELENOR_SPILL' in the view name, along with the specific product keys, suggests it's likely focused on particular Telenor-related 'spill' products or services.

## Data Sources (Inputs)
- ← [[GALAXY.AGREEMENT_DETAIL_FACT]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]

