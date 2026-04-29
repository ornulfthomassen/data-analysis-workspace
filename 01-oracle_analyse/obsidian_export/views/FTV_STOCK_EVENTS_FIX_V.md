# FTV_STOCK_EVENTS_FIX_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies and categorizes monthly subscription events, specifically focusing on 'churn' (CHURN_VULA) and 'growth/addition' (TILVEKST_UTBYGGING, TILVEKST_OFFNET) events for broadband subscriptions. It achieves this by comparing current and previous month's subscription product states, linking to VULA (Virtual Unbundled Local Access) records for churn, and product details for growth, then pivots the results to provide event counts per subscription per month, along with an associated identifier (VULA ID for churn, Product Key for growth).

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_FTV_MONTH_AGG_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| BB_SUBSCRIPTION_KEY |
| TV_SUBSCRIPTION_KEY |
| BB_SOURCE_SYSTEM |
| TV_TYPE |
| P3_BB_PRODUCT_KEY |
| P4_BB_PRODUCT_KEY |
| P3_TV_PRODUCT_KEY |
| P4_TV_PRODUCT_KEY |
| P3_BB_PRIM_PRODUCT_KEY |
| P4_BB_PRIM_PRODUCT_KEY |
| NUM_SUBS |
| RUN_DT_KEY |
- ← [[GALAXY.SUBSCRIPTION_DIM]]
| Column Name |
|---|
| SUBSCRIPTION_KEY |
| SUBSCR_USER_LOC_KEY |
| SUBSCR_FWA_LOC_KEY |
- ← [[CCM.VYA_FTV_MISSING_FAR_ID]]
| Column Name |
|---|
| INSTALL_LOC_KEY |
| SUBSCRIPTION_KEY |
- ← [[VULA.LOAD_VULA_WEB]]
| Column Name |
|---|
| CONFIRMED_UP_DATE |
| ID |
| FAR_ID |
| STATE |
| CONSENT |
| CEDING_ISP |
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
| Column Name |
|---|
| SUBSCRIPTION_KEY |
| SUB_PROD_START_DT_KEY |
| SUB_PRODUCT_KEY |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |

