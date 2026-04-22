# GCP_SUBSCRIPTION_EVENTS

**Schema:** `CCM` | **Type:** `View`

## Description
Provides subscription-level event data, including contextual numeric fields, primarily used by CI MA (Customer Intelligence Marketing Automation) to generate sales tips. It filters out certain events (event_id=32, speed reduction) that did not occur in the current month.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_SUBSCRIPTION_EVENTS]]

