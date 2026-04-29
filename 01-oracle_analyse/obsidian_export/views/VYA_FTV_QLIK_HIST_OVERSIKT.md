# VYA_FTV_QLIK_HIST_OVERSIKT

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates historical data for various Key Performance Indicators (KPIs) related to product adoption, growth (tilvekst), and churn across different business units (selskap), product technologies, and customer segments. It transforms and categorizes raw data from a source table into a structured format suitable for analytical reporting, likely for a tool like Qlik, focusing on opening and closing balances, various types of growth, and different churn reasons.

## Data Sources (Inputs)
- ← [[CLM_ADM.FTV_QLIK_HIST_OVERSIKT]]
| Column Name |
|---|
| Periode |
| selskap |
| produkt teknologi type |
| Kategori |
| produkt kunde segment |
| produkt volum grp |
| IB |
| Tilvekst Utbygging |
| Tilvekst Offnet |
| Tilvekst Onnet |
| NettoTek Crossover |
| Churn Flytting |
| Churn Konkurrent |
| Churn Vula |
| Churn Annen |
| Admin |
| UB |

