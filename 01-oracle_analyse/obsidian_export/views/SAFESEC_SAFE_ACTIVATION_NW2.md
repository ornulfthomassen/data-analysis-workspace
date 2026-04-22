# SAFESEC_SAFE_ACTIVATION_NW2

**Schema:** `CCM` | **Type:** `View`

## Description
This view calculates the latest activation dates for various 'Safe and Secure' features (VPN activation, Email monitoring activation, and Credit Card monitoring activation) for each customer. It aggregates specific action descriptions from a safety usage log and links them to customer information, serving as a foundational dataset for a 'SAFE dashboard'.

## Data Sources (Inputs)
- ← [[clm_ccm.v_ccm_agrm_sfty_use]]
- ← [[clm_adm.adm_customer_mapping]]
- ← [[galaxy.date_dim_mv]]

