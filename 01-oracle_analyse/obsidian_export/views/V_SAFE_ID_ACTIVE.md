# V_SAFE_ID_ACTIVE

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates and counts specific identity-related security actions (email verification for ID monitoring, adding monitored credit cards, and creating VPN tokens) by customer, customer lifecycle segment, and activation date.

## Data Sources (Inputs)
- ← [[CLM_CCM.v_ccm_agrm_sfty_use]]
- ← [[CLM_ADM.adm_customer_mapping]]
- ← [[CLM_CCM.ccm_customer_info_2]]

