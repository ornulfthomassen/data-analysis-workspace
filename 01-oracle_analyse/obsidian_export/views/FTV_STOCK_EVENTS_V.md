# FTV_STOCK_EVENTS_V

**Schema:** `CCM` | **Type:** `View`

## Description
Identifies and categorizes key lifecycle events for broadband/TV subscriptions on a monthly basis. It tracks subscription ends (potentially linked to VULA churn processes) and new subscription starts (categorized by build-out types like 'UTBYGGING' or 'OFFNET'), then pivots these events to provide aggregated counts of each event type per subscription and month, alongside an associated event identifier.

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
| FAR_ID |
| STATE |
| CONFIRMED_UP_DATE |
| CONSENT |
| CEDING_ISP |
| ID |
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

