# SAFESEC_SAFE_ACTIVATION_NW2

**Schema:** `CCM` | **Type:** `View`

## Description
This view calculates the latest activation dates for various security features (VPN, Email monitoring, Credit Card monitoring) for each customer. It consolidates these dates, defaulting to an early date if a feature has not been activated. The view is intended as a data source for a SAFE dashboard.

## Data Sources (Inputs)
- ← [[clm_ccm.v_ccm_agrm_sfty_use]]
| Column Name |
|---|
| action_description |
| last_date |
| kurt_id |
| first_date |
- ← [[clm_adm.adm_customer_mapping]]
| Column Name |
|---|
| customer_sk |
| kurt_id |
- ← [[galaxy.date_dim_mv]]
| Column Name |
|---|
| day |
| year_week_number |
| last_week |

