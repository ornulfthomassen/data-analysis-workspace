# DUAL_ACCOUNT_RAPPORT_0B

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Identifies and reports inconsistencies and relationships between MSISDNs (mobile numbers) and user IDs across various customer management and identity management systems (CM, COMOYO FIM, and COMOYO USER_SERVICES). It aims to detect 'dual account' scenarios or discrepancies in service provisioning and user verification by combining different scenarios related to how these identifiers are associated and categorizing them with descriptive information.

## Data Sources (Inputs)
- ← [[CM.SUBSCRIPTION]]
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]
- ← [[COMOYO.FIM_USER]]
- ← [[COMOYO.FIM_USER_PHONES]]
- ← [[COMOYO.FIM_USER_ACCOUNTS]]
- ← [[COMOYO.FIM_USER_EMAILS]]
- ← [[COMOYO.USER_SERVICES_PHONES]]
- ← [[COMOYO.USER_SERVICES]]

