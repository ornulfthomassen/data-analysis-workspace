# DUAL_ACCOUNT_RAPPORT_0C

**Schema:** `CCM` | **Type:** `View`

## Description
Identifies 'dual accounts' by linking subscriptions in the 'CM' system with user information (FIM_USER, FIM_USER_PHONES) and user services data (USER_SERVICES_PHONES) in the 'COMOYO' system. Specifically, it flags accounts where a phone number (MSISDN) associated with a 'Connect ID' in the CM system is either unverified or lacks a verification timestamp in the FIM_USER_PHONES system, while also appearing in the USER_SERVICES_PHONES for the same Connect ID. The purpose is to report on phone numbers linked to a Connect ID that are either unverified or have missing verification timestamps across different systems, indicating potential data inconsistencies or security concerns related to verification status.

## Data Sources (Inputs)
- ← [[CM.SUBSCRIPTION]]
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]
- ← [[COMOYO.FIM_USER]]
- ← [[COMOYO.FIM_USER_PHONES]]
- ← [[COMOYO.USER_SERVICES_PHONES]]

