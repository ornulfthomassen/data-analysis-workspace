# TST_FTV_STOCK_EVENTS_V

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates and pivots broadband subscription lifecycle events on a monthly basis. It categorizes events into 'CHURN_VULA', 'TILVEKST_UTBYGGING' (new build-out growth), and 'TILVEKST_OFFNET' (new off-net growth), providing a count for each event type per subscription and month. It also carries an 'EXTRA_01' column which identifies the VULA ID for churn events or the Product Key for growth events.

## Data Sources (Inputs)
- ← [[CCM.SUBSCR_FTV_MONTH_CURRENT_AGG_V_DEV1]]
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
| SUBSCRIPTION_KEY |
| INSTALL_LOC_KEY |
- ← [[VULA.LOAD_VULA_WEB]]
| Column Name |
|---|
| FAR_ID |
| CONFIRMED_UP_DATE |
| ID |
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

