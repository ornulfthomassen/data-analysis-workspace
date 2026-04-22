# VYA_FTV_QLIK_STOCK

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive dataset for analyzing product/service stock, growth (tilvekst), and churn metrics, integrated with detailed date dimensions. It consolidates key performance indicators (KPIs) like opening and closing balances, various growth factors, and different types of churn, alongside product and service attributes. The view is designed to support reporting, likely for Qlik, by ensuring all relevant date periods (daily, weekly, monthly for years 2022-2024) are included, even if stock data is not present for every period.

## Data Sources (Inputs)
- ← [[CLM_ADM.FTV_QLIK_STOCKAPP]]
- ← [[GALAXY.DATE_DIM_MV]]

