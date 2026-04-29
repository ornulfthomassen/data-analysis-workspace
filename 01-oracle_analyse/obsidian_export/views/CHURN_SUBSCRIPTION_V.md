# CHURN_SUBSCRIPTION_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view prepares a filtered dataset of subscription information, specifically for 'MPP' product groups within the last 24 months up to the current month. It extracts various details like customer, dealer, device, and revenue information, and calculates a revenue-to-monthly-fee ratio, likely for churn analysis.

## Data Sources (Inputs)
- ← [[CLM_ADM.CHURN_ADM_SUBSCRIPTION]]
| Column Name |
|---|
| period_month |
| period_month_date |
| subscription_sk |
| main_number_sk |
| customer_sk_owner |
| customer_sk_user |
| dealer_chain |
| dealer_name |
| device_producername |
| device_modelname |
| changetype |
| in_port_sp_group |
| mb_last1 |
| net_revenue_adj |
| no_days_mno_start |
| no_days_subs_start |
| no_mb_pct_last1 |
| no_porting |
| profit_cat |
| prod_attr_incl_mb |
| prod_attr_mth_fee |
| product_family |
| product_name |
| sales_ch |
| subs_start_reason |
| next_familie_rabatt_status |
| swap_status |
| product_group |

