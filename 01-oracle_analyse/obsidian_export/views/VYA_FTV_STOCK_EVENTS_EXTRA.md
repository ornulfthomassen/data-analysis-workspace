# VYA_FTV_STOCK_EVENTS_EXTRA

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies and categorizes key subscription events, specifically 'CHURN_VULA' (VULA-related churn) and 'TILVEKST' (growth, split into 'UTBYGGING' and 'OFFNET' based on product keys). It aggregates these events by month and subscription, providing a count for each event type along with an `EXTRA_01` identifier (VULA ID for churn, Product Key for growth). The view aims to provide a summarized monthly stock of these events per subscription, determining subscription end/start points based on product key changes and associating them with relevant external data (VULA, product details).

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_FTV_MONTH_AGG_V]]
| Column Name |
|---|
| BB_SUBSCRIPTION_KEY |
| PERIOD_MONTH_KEY |
| P1_BB_PRODUCT_KEY |
| P2_BB_PRODUCT_KEY |
| P3_BB_PRODUCT_KEY |
| P4_BB_PRODUCT_KEY |
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
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |

