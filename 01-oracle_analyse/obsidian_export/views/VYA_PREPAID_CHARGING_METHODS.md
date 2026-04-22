# VYA_PREPAID_CHARGING_METHODS

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates prepaid mobile charging method statistics. It calculates the total gross amount charged (including VAT), the number of distinct accounts involved, and the total number of charging events (lading/loads) for specific traffic types categorized as 'EDR' and 'Ladinger'. The results are grouped by period and traffic type for an overview of charging activities.

## Data Sources (Inputs)
- ← [[CCDW_USAGE.MOBILE_SUBSCR_CHARGE_MONTH]]
- ← [[GALAXY.TRAFFIC_TYPE_DIM_V]]

