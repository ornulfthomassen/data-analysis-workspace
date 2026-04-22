# VYA_STOCK_MOBILE_MONTH_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates monthly and daily mobile subscription stock data, calculating unbilled (UB_MONTH), invoiced (IB_MONTH), and net (NETTO) balances, along with total discounts. It categorizes this data by various dimensions including product key, profit categories (TALE_PROFIT_CAT_NAME2, TALE_PROFIT_CAT_NAME4, TALE_PROFIT_CAT_NAME7), customer lifecycle segments (CLM_LIVSFASE_SEGMENT_NAME_O), owner and user age groups, and family bonus flags. The view combines historical monthly data with current month's daily data (up to yesterday) to provide a comprehensive, rolling 24-month view of mobile stock and its financial components.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
- ← [[CLM_ADM.STOCK_MOBILE_HISTORY_MONTH_AGG]]
- ← [[CRM_ANALYSE.ADM_CLM_LIVSFASE_DIM]]
- ← [[CRM_ANALYSE.ADM_PROFIT_CAT_DIM]]
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
- ← [[CLM_ADM.STOCK_MOBILE_HISTORY_DAY_AGG]]

