# VYAMN_CONTACTS_STG_CI360

**Schema:** `CCM` | **Type:** `View`

## Description
This view integrates customer contact and interaction data from SAS360_COMMON.SAS360_CONTACTS with associated marketing campaign metadata, customer mapping details, supplementary subject information (such as subscriptions and FAR IDs), and product dimensions. Its primary purpose is to prepare and stage a comprehensive dataset of 'KIM Contact-data' for loading into a downstream data warehouse (referred to as Mjøsa), providing a rich and enriched view of customer interactions for analytical and reporting purposes.

## Data Sources (Inputs)
- ← [[SAS360_COMMON.SAS360_CONTACTS]]
- ← [[SAS360_COMMON.SAS360_CONTACTS_METADATA_KIM]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
- ← [[SAS360_COMMON.SAS360_SUPPL_SUBJECTS]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[CLM_CCM.PRODUCT_DIM_V]]

