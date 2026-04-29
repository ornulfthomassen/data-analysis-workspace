# KIM_NEWSLETTER_V

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates campaign performance metrics (volume, sales, presented items, all sales) and customer response data for a specific campaign ('C4') and date range (after 2017-01-01). It combines data from campaign details, customer responses, and dimension tables (channel and response), grouping the results by program, campaign, activity, and response information.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_V]]
| Column Name |
|---|
| VOLUME |
| KPI_SALES |
| KPI_PRESENTED |
| KPI_ALL_SALES |
| PROGRAM |
| CAMPAIGN |
| ACTIVITY_NAME |
| ACTIVITY_ID |
| ACTIVITY_DESC |
| CONTACT_KEY |
| CHANNEL_KEY |
| RESPONSE_KEY |
| contact_date_key |
| CAMPAIGN_ID |
- ← [[CRM_ANALYSE.KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| CONTACT_KEY |
| EXTERNAL_RESPONSE_INFO_ID1 |
| EXTERNAL_RESPONSE_INFO_ID2 |
- ← [[KIM_CHANNEL_DIM]]
| Column Name |
|---|
| CHANNEL_KEY |
- ← [[KIM_RESPONSE_DIM]]
| Column Name |
|---|
| RESPONSE_KEY |
| RESPONSE_NM |

