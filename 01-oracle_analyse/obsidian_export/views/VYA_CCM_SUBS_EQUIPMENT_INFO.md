# VYA_CCM_SUBS_EQUIPMENT_INFO

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates comprehensive information about customer subscriptions, including details of the associated SIM cards, the devices (handsets) used with those subscriptions, and related agreement data such as insurance and device swap agreements. It links subscription-level equipment data with device dimensions, historical aggregates, and specific agreement terms to provide a holistic view of 'Subscription Equipment Information'. It is noted to be used for loading order data to another system (MJØSA).

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_SUBS_EQUIPMENT_INFO_V]]
- ← [[CLM_CCM.CCM_HANDSET_DIM_V]]
- ← [[CLM_ADM.ADM_DEVICE_RANGE_DIM]]
- ← [[CLM_ADM.ADM_HANDSET_HIST_AGG]]

