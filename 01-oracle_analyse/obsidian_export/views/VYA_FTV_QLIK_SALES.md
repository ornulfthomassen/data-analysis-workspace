# VYA_FTV_QLIK_SALES

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates detailed sales order data with date dimension attributes. It categorizes and transforms key order-related fields such as value chain, source system, technology, and order type, and aggregates order counts. The view also enriches the sales records with comprehensive date and time-based attributes, providing a unified dataset for sales analysis and reporting, specifically designed for Qlik applications.

## Data Sources (Inputs)
- ← [[CLM_FIXED_CCM.QLIK_SALES_APP_ORDER]]
| Column Name |
|---|
| ORDER_SOURCE |
| ORDER_VALUECHAIN |
| ORDER_TYPE |
| ORDER_TECHNOLOGY |
| ORDER_DATE_F |
| ORDER_DATE_STOCK |
| ORDER_DATE_EXP_STOCK |
| SUB_SEGMENT |
| ORDER_SALES_MAPPING |
| ORDER_BB_SPEED |
| ORDER_BB_SPEED_FROM |
| ORDER_CABIN |
| ORDER_CHANNEL |
| ORDER_CHANNEL_L2 |
| ORDER_DEALER |
| ORDER_KPI |
| ORDER_CONNECTION_TYPE |
| ORDER_STATUS_L6 |
| SALGSRUNDE_ID |
| SALGSRUNDE_NAVN |
| DU_PROJECT_QA |
| ORDER_REVENUE_RECURRING |
| ORDER_REVENUE_NONRECURRING |
| ORDER_HW_DECODER |
| ORDER_HW_ROUTER |
| ORDER_HW_EXTENDER |
| ADRESSE_TYPE |
| GEO_GRUNNKRETSNR |
| GEO_KOMMUNE |
| GEO_FYLKE |
| ORDER_CAMPAIGN_ID |
| CAMPAIGN_GROUP_ID |
| CAMPAIGN_TYPE |
| CAMPAIGN_SALES_SUBTYPE |
| CAMPAIGN_SIZE_DETAILED |
| CAMPAIGN_NAME |
| CAMPAIGN_PERIOD_MTH |
| CAMPAIGN_TECHNOLOGY |
| ORDER_FC_VERSION |
| ORDER_TARGET_VERSION |
| ORDER_FC_COUNT |
| ORDER_TARGET_COUNT |
| ORDER_COUNT |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| "DAY" |
| DATE_KEY |
| DAY_OF_WEEK |
| DAY_OF_WEEK_SHORT |
| TYPE_OF_DAY |
| WEEK_NUMBER |
| YEAR_WEEK_NUMBER |
| "YEAR" |
| MONTH_NAME |
| MONTH_SHORT_NAME |
| MONTH_NUMBER |
| YEAR_MONTH_NUMBER |
| RELATIVE_MONTH |
| RELATIVE_WEEK |

