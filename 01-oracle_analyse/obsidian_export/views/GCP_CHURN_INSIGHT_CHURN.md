# GCP_CHURN_INSIGHT_CHURN

**Schema:** `CCM` | **Type:** `View`

## Description
This view is designed to provide comprehensive customer and subscription-level data for churn analysis and insights. It consolidates various metrics including customer demographics (age, gender, segment), subscription details (product family, name, sales channel), financial indicators (net revenue, monthly fee), usage statistics (MB usage, days since subscription start), and critical churn-related KPIs (churn flags, porting outbound, termination flags). The data is prepared with specific rounding and casting for analytical purposes related to churn prediction and understanding.

## Data Sources (Inputs)
- ← [[CLM_ADM.CHURN_INSIGHT_CHURN]]

