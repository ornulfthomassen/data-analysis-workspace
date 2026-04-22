# VYAMN_CONTACTS_STG_CI360_T

**Schema:** `CCM` | **Type:** `View`

## Description
This view is a test view designed to process and prepare contact data and associated metadata from SAS CI360. Its purpose is to act as a staging area, converting data types as needed, to serve as the main source for loading contacts and contact metadata into the KIM system. It aims to replace an existing view (CCM.VYAMN_CONTACTS_STG_CI360).

## Data Sources (Inputs)
- ← [[SAS360_COMMON.SAS360_CONTACTS]]
- ← [[SAS360_COMMON.SAS360_CONTACTS_METADATA_KIM]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
- ← [[SAS360_COMMON.SAS360_SUPPL_SUBJECTS]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]

