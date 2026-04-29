# CHURN_CUST_SUBSCR_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Combines subscription details with owner and user customer demographic and behavioral data for churn analysis. It links subscriptions to their primary owner and actual user, providing a comprehensive view for analytical purposes, and identifies relationships between owner and user.

## Data Sources (Inputs)
- ← [[CLM_ADM.CHURN_SUBSCRIPTION_v]]
| Column Name |
|---|
| cu_customer_sk_owner |
| mpp_customer_sk_user |
| PERIOD_MONTH_KEY |
| PERIOD_MONTH_DATE |
| SUBSCRIPTION_KEY |
| MPP_MAIN_ID_SK |
| MPP_DEALER_CHAIN |
| MPP_DEALER_NAME |
| MPP_DEVICE_PRODUCERNAME |
| MPP_DEVICE_MODELNAME |
| MPP_CHANGETYPE |
| MPP_IN_PORT_SP_NAME |
| MPP_MB_LAST1 |
| MPP_NET_REVENUE_ADJ |
| MPP_NO_DAYS_MNO_START |
| MPP_NO_DAYS_SUBS_START |
| MPP_NO_MB_PCT_LAST1 |
| MPP_NO_PORTING |
| MPP_PROFIT_CAT |
| MPP_PROD_ATTR_INCL_MB |
| MPP_PROD_ATTR_MTH_FEE |
| MPP_PRODUCT_FAMILY |
| MPP_PRODUCT_NAME |
| MPP_SALES_CH |
| MPP_SUBS_START_REASON |
| MPP_NEXT_FAMILIE_RABATT_STATUS |
| MPP_SWAP_STATUS |
| REVENUE_FEE_RATIO |
- ← [[CLM_ADM.CHURN_CUSTOMER_v]]
| Column Name |
|---|
| cu_age |
| cu_gender |
| clm_livsfase_segment |
| cu_net_revenue |
| cu_no_fbr |
| cu_no_mbb |
| cu_no_mpp |
| cu_no_mpr |
| cu_no_prod_cat |
| period_month_key |
| customer_sk |

