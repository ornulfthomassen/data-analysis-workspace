# VYA_CDC_PHONE_NUMBER

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a combined dataset of phone number details and associated historical subscription master information. Its primary purpose appears to be to retrieve phone numbers linked to specific periods of subscription records, while also obfuscating (masking) the national part of the phone number for data privacy or security reasons. It includes registration, change, and deletion tracking information for the phone numbers.

## Data Sources (Inputs)
- ← [[CDC.PHONE_NUMBER]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]

