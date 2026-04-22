# VYA_CDC_EMAIL_ADDRESS

**Schema:** `CCM` | **Type:** `View`

## Description
This view retrieves email address records from the `CDC.EMAIL_ADDRESS` table. Its primary function is to apply a complex obfuscation or masking logic to the `EMAIL_ADDRESS` field, likely for data privacy or anonymization purposes. It also identifies and flags email addresses that are malformed (e.g., missing an '@' symbol or containing multiple '@' symbols). Additionally, it exposes registration and change audit information associated with these records.

## Data Sources (Inputs)
- ← [[CDC.EMAIL_ADDRESS]]

