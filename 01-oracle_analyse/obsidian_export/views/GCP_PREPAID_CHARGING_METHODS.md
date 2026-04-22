# GCP_PREPAID_CHARGING_METHODS

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates prepaid mobile subscription charging data for reporting purposes, specifically for SAS Viya. It calculates the total gross amount (SUM_INKLUDERT_MVA), the number of distinct accounts (ANTALL_KONTO), and the total number of charges/events (ANTALL_LADINGER) for prepaid charging methods. The data is grouped by period, traffic type ID, and traffic type name, and filtered for 'EDR' and 'Ladinger' traffic types.

## Data Sources (Inputs)
- ← [[CCDW_USAGE.MOBILE_SUBSCR_CHARGE_MONTH]]
- ← [[GALAXY.TRAFFIC_TYPE_DIM_V]]

