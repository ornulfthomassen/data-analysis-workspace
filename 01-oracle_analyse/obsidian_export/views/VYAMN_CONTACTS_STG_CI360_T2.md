# VYAMN_CONTACTS_STG_CI360_T2

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `VYAMN_CONTACTS_STG_CI360_T2`, is a staging view designed to extract, transform, and consolidate contact event data and related metadata. Its primary purpose is to replace an existing view (`CCM.VYAMN_CONTACTS_STG_CI360`) as the main source for loading contact information and its metadata into the KIM system. It combines contact records with campaign details, customer mapping, supplemental subject data, subscription master historical data, and product dimensions, performing various data type conversions and derivations.

## Data Sources (Inputs)
- ← [[SAS360_COMMON.SAS360_CONTACTS]]
- ← [[SAS360_COMMON.SAS360_CONTACTS_METADATA_KIM]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
- ← [[SAS360_COMMON.SAS360_SUPPL_SUBJECTS]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[CLM_CCM.PRODUCT_DIM_V]]

