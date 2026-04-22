# VYAMN_RESPONSES_STG_CI360_T2

**Schema:** `CCM` | **Type:** `View`

## Description
This view is a test view designed to extract and transform contact and response metadata from SAS360 systems. Its purpose is to process customer responses, enriching them with customer, subscription, and main number details. If successful, it will replace 'CCM.VYAMN_CONTACTS_STG_CI360' as the primary source for loading contacts and related metadata into the KIM system.

## Data Sources (Inputs)
- ← [[SAS360_COMMON.SAS360_RESPONSES]]
- ← [[SAS360_COMMON.SAS360_CI_RESPONSE]]
- ← [[SAS360_COMMON.SAS360_CCM_RESPONSE_REASON]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
- ← [[SAS360_COMMON.SAS360_SUPPL_SUBJECTS]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]

