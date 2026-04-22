# PI_PRICING_HIST_UP

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a dataset for tracking price changes on specific call plans ('ringeplaner'). The data is intended to be loaded into Viya for analysis and monitoring of these pricing updates. It consolidates various pricing and subscription-related attributes, including historical pricing details for both current and previous states (indicated by 'IB_' for 'inbound'/'initial' and 'UB_' for 'upgraded'/'updated').

## Data Sources (Inputs)
- ← [[adhoc_bs.mk_2233_tmp]]

