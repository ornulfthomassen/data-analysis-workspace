# DUAL_ACCOUNT_RAPPORT_0B1

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies and reports on the mapping status and relationships between 'Connect IDs' from the 'CM' system (CM_CID) and 'TD' system (TD_CID_USER, sourced from COMOYO.FIM_USER) for mobile subscriptions (MSISDNs). It specifically highlights two scenarios:
1.  Active subscriptions where a CM_CID is present for a specific offer type (PARAMETER_ID = 2100) but lacks a corresponding TD_CID_USER entry.
2.  Closed subscriptions that still have an 'open' CM_CID (active offer configuration) and their mapping status to TD_CID_USER. 
The purpose is to detect potential 'dual account' issues or inconsistencies in 'TnN service provisioning' and user identity management across different systems.

## Data Sources (Inputs)
- ← [[CM.SUBSCRIPTION]]
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]
- ← [[COMOYO.FIM_USER]]

