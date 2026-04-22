# VYA_CCM_CUSTOMER_INFO_2

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates and categorizes comprehensive customer information, including product ownership/usage counts across various service types (mobile, fixed-line, broadband, TV, SWAP, device insurance) and agreement statuses. It also derives detailed customer profiles (consumer/business, owner/user) based on their product portfolio. The view is explicitly noted for loading detailed customer segment and product relationship data into a data warehouse (referred to as 'Mjøsa'), and includes a default entry for unknown customer IDs.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CLM_CCM.CCM_CUSTOMER_INFO_2_V]]

