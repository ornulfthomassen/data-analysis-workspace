# VYA_ADM_ORDEN_ACTIVATION_SUBS

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides an administrative overview of 'Orden' subscription activations. It combines subscription offer details with 'Orden'-specific incentives and their latest activation history. The view calculates the number of days waited between the 'Orden' offer becoming available and the actual signup date, and includes flags and dates related to 'Orden' availability and first signup for each subscription.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_ORDEN_ACTIVATION_HIST]]
- ← [[ODS.SUBSCRIBED_OFFER_ODS_MOB]]
- ← [[CM.SUBSCRIPTION_OFFER_INCENTIVE]]

