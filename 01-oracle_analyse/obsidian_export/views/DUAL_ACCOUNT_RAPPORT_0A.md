# DUAL_ACCOUNT_RAPPORT_0A

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view identifies and reports on 'dual account' discrepancies related to TnN mobile service provisioning and the relationship between MSISDNs and Connect IDs. Specifically, it flags accounts that are missing an MSISDN ('ACC_MSISDN = 'null'') and have an 'ACC_USER_ID' starting with 'tnn_mobile_0%'. It categorizes these issues based on whether the corresponding subscription (from CM.SUBSCRIPTION) is closed or open, and checks for correct or problematic linkages with 'Connect IDs' (from CM.SUBSCRIBED_OFFER_CONFIGURATION, identified by PARAMETER_ID = 2100). The view aims to highlight situations requiring manual intervention due to missing MSISDNs and potential inconsistencies in how TnN services are associated with Connect IDs, differentiating between active and inactive subscriptions.

## Data Sources (Inputs)
- ← [[COMOYO.FIM_USER]]
- ← [[COMOYO.FIM_USER_ACCOUNTS]]
- ← [[CM.SUBSCRIPTION]]
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]

