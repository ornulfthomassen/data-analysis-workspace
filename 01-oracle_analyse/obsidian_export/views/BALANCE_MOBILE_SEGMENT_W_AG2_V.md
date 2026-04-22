# BALANCE_MOBILE_SEGMENT_W_AG2_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and segments mobile customer balance data, adjusted for terminations and outports. It provides a detailed analytical dataset by combining balance information with various dimensions such as refresh date, period keys (week, month, year), product details (description, key, name), payment methods, brand, binding status, profit categories, and multiple customer segmentation attributes (variable segment, churn segment, lifecycle segment, MAP2 segment). The data is filtered to exclude certain product descriptions (e.g., 'BEDRIFT', 'DEMO', 'TVILLING', 'FASTNETT', 'SPONS', 'PRIVAT') and is restricted to records from a specific period (PERIOD_WEEK_KEY >= 201729). Missing descriptive values are replaced with 'Ukjent' or -1 for consistency.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.BALANCE_MOBILE_SEGMENT_W_AGG]]

