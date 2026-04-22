# CHURN_FORECAST_ST_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `CHURN_FORECAST_ST_V`, consolidates a comprehensive dataset for potential churn analysis or forecasting. It combines mobile subscription history, porting event details, customer information, product configurations, and profit segmentation data. The view focuses on mobile subscriptions within specific market areas (2 and 4) for porting orders with statuses 'IB', 'FB', or 'KB', specifically for data within the last 24 months. It enriches porting and order information with customer, product, and historical subscription attributes, and attempts to derive a 'PROFIT_CAT' from multiple sources.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.MPORT_PORT_REPORT]]
- ← [[CRM_ANALYSE.MPORT_PORT_REPORT_EXTRA_INFO]]
- ← [[CRM_ANALYSE.ADM_MOBIL_SUBSCR_HIST]]
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
- ← [[CRM_ANALYSE.PROFITSEGMENT_MOBILE]]
- ← [[PROFIT.CP_CAT_BED_PRIV]]

