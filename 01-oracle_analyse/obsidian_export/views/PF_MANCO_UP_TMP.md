# PF_MANCO_UP_TMP

**Schema:** `CCM` | **Type:** `View`

## Description
This view transforms and presents a comprehensive set of performance metrics and customer/agreement attributes for a specific period (identified by week number). It includes details like age, life stage, sales channels, agreement dates, product descriptions, and various key performance indicators (KPIs) related to email, credit card, VPN activations/terminations, and 'safe' categories (new sales, terminations, stock).

## Data Sources (Inputs)
- ← [[adhoc_bs.ah_2343_manco]]
| Column Name |
|---|
| period_week |
| last_week |
| agreement_key |
| source_agreement_offer_id |
| customer_sk |
| age |
| age_group |
| clm_livsfase_segment_name |
| mine_sider |
| mitt_telenor |
| NW_sales_channel |
| NW_dealer_chain |
| RM_sales_channel |
| RM_dealer_chain |
| migrated |
| agrm_start_date |
| agrm_end_date |
| agrm_duration |
| agrm_start_week |
| agrm_end_week |
| product_desc |
| ema_year_week_number |
| days_to_eMail_activation |
| cc_year_week_number |
| days_to_cc_activation |
| vpn_year_week_number |
| KPI_new_eMail_activation |
| KPI_eMail_activated |
| KPI_eMail_terminated |
| KPI_new_Creditcard_reg |
| KPI_Creditcard_registered |
| KPI_Creditcard_terminated |
| KPI_new_VPN_activation |
| KPI_VPN_registered |
| KPI_VPN_terminated |
| KPI_new_safe |
| Kpi_new_safe |
| KPI_term_safe |
| KPI_stock_safe |

