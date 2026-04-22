# V_TEST_ANALYSE_MART

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `V_TEST_ANALYSE_MART`, serves as a comprehensive analytical data mart, combining various aggregated customer, product, usage (mobile, fixed, internet), and financial metrics. It joins data from two aggregated views based on period month, main number, and user customer key to provide a holistic view for CRM analysis and reporting. The data includes details like customer identifiers, product attributes, market area, business area, subscription counts, call minutes, SMS/MMS numbers, data volumes, and revenue figures (net and gross).

## Data Sources (Inputs)
- ← [[crm_analyse.v_analyse_use_agg_mainnumber]]
- ← [[CRM_analyse.v_analyse_con_subscr_agg]]

