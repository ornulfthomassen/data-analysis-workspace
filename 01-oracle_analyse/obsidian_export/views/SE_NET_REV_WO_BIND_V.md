# SE_NET_REV_WO_BIND_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view calculates the aggregated net revenue (total of initiation, periodic, and discount fees) on a monthly basis for each subscription. It filters for specific market areas (likely Sweden, based on context) and 'Mobil Telefoni' (Mobile Telephony) products, explicitly excluding any revenues associated with 'Terminalbinding' (terminal binding) product types. The primary purpose is to provide net revenue figures for mobile subscriptions that are not tied to a device binding.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_FEE_MONTH_FACT_V]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.SUBSCRIPTION_DIM_MV]]

