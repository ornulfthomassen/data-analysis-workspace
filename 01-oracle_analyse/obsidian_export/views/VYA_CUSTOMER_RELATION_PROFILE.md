# VYA_CUSTOMER_RELATION_PROFILE

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates customer relation profiling data from 'customer_relation_profile_fact' with customer mapping information from 'ADM_CUSTOMER_MAPPING'. It focuses on active customer records (profiling_end_dt_key = 99991231 and specific MAP_STATUS values) to provide counts for various mobile and fixed-line services, along with associated flags and bonus data.

## Data Sources (Inputs)
- ← [[galaxy.customer_relation_profile_fact]]
| Column Name |
|---|
| customer_relation_key |
| num_mobile_telephony_prepaid |
| num_mobile_broadband |
| num_mobile_telemetry |
| num_mobile_telephony_business |
| num_mobile_broadband_business |
| num_swap |
| num_swap_plus_insurance |
| family_bonus_flag |
| databonus_gb |
| secureid_flag |
| num_ftv_fixed_telephony_bbt |
| num_ftv_fixed_broadband_coax |
| num_ftv_fixed_broadband_fiber |
| num_ftv_fixed_tv |
| num_fixed_telephony_isdn |
| num_fixed_telephony_pstn |
| num_fixed_telephony_bbt |
| num_fixed_broadband_adsl |
| num_fixed_broadband_vdsl |
| num_fixed_broadband_fiber |
| num_fixed_broadband_wimax |
| current_status |
| profiling_start_dt_key |
| profiling_end_dt_key |
| CUSTOMER_KEY |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |
| MAP_STATUS |

