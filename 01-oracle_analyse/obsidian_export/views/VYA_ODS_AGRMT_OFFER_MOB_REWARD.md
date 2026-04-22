# VYA_ODS_AGRMT_OFFER_MOB_REWARD

**Schema:** `CCM` | **Type:** `View`

## Description
This view combines agreement offer and mobile reward data (including agreement IDs, product details, and status) with customer mapping information. It enriches the data by deriving a more descriptive product status, transforming customer identifiers, and adding load-specific metadata (volume, load datetime). According to the comments, its primary purpose is to prepare and load `ODS_AGREEMENT_REWARD` data into a target system or data warehouse referred to as 'Mjøsa'.

## Data Sources (Inputs)
- ← [[CLM_CCM.V_ODS_AGRMT_OFFER_MOB_REWARD]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]

