# CHURN_SUBSCR_USR_TO_OWN_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view identifies and flags instances within 'MPP' product group subscriptions where the primary user of the subscription becomes its owner, following a change in the assigned owner. For such events, it records the date of this ownership change and calculates the duration (in months) of the preceding period. The data is filtered to include only MPP subscriptions and is restricted to a rolling window of the last 25 months, likely for churn analysis related to ownership transfers.

## Data Sources (Inputs)
- ← [[CLM_ADM.CHURN_ADM_SUBSCRIPTION]]

