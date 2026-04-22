# ORDER_LINE_DETAIL_FACT_V_BCK

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive and consolidated source of detailed order line information for mobile services. It integrates a wide array of attributes and Key Performance Indicators (KPIs) from a primary order line fact table with related customer, subscription, and time dimension data. The view is designed for extensive analytical reporting and business intelligence, covering aspects such as new sales, product changes, porting activities, terminations, churn, campaign performance, and device management. The `_BCK` suffix in the view name might indicate a backup, a historical snapshot, or a specific version of the fact view.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_MOB_FACT_MV]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[GALAXY.ORDER_TIME_DIM_V]]

