# BALANCE_MOBILE_SEGMENT_AGG_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and segments mobile balance data from two distinct sources ('BALANCE_MOBILE_SEGMENT_AGG' and 'BALANCE_TALKMORE_AGG') for CRM analysis. It calculates a net balance by subtracting 'OUT_PORT' for the first source. The view enriches the data with month dimension details (current and previous periods) and product dimension details for the Talkmore segment. It applies extensive filtering based on product descriptions to exclude certain categories (e.g., business, demo, twin, specific SMS/fixed-line products, private, and specific Talkmore products). Additionally, it transforms specific lifecycle segment names ('Barn' to 'Småbarnsfamilie', 'Ungdom' to 'Etablert barnefamilie') and handles null values by assigning 'Ukjent' (Unknown) or default numeric values. The final dataset is filtered to include data from December 2014 onwards, providing a consolidated, segmented, and cleaned view of mobile subscriber balances.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.BALANCE_MOBILE_SEGMENT_AGG]]
- ← [[ADM_MONTH_DIM]]
- ← [[CLM_ADM.BALANCE_TALKMORE_AGG]]
- ← [[GALAXY.PRODUCT_DIM]]

