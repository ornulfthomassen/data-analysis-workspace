# VYAMN_RESPONSES_STG_CI360_T

**Schema:** `CCM` | **Type:** `View`

## Description
This view extracts, transforms, and enriches raw customer response data from the SAS360 system, primarily focusing on response details, associated customer information, and subscription details. It processes response IDs, timestamps, channels, and links them to customer and subscription master data to create a comprehensive staging record, suitable for further analysis or loading into a data warehouse related to customer intelligence (CI360). It calculates various date keys (month, week, date key) and maps identifiers like customer SK, subscription SK, and main number SK.

## Data Sources (Inputs)
- ← [[SAS360_COMMON.SAS360_RESPONSES]]
- ← [[SAS360_COMMON.SAS360_CI_RESPONSE]]
- ← [[SAS360_COMMON.SAS360_CCM_RESPONSE_REASON]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
- ← [[SAS360_COMMON.SAS360_SUPPL_SUBJECTS]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]

