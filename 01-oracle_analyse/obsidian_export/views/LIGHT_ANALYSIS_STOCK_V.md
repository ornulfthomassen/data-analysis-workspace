# LIGHT_ANALYSIS_STOCK_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates detailed information about customer subscriptions, including user and owner demographics (household size, municipality, address, age, gender), customer lifecycle and segmentation data, product details (family, name, area, group, reporting, payment, price, data included, type, dates), and handset specifications (camera, type, manufacturer, OS, network class). It links subscriptions to customers, households, addresses, products, and handsets, providing a comprehensive dataset for analytical purposes, particularly for understanding subscriber profiles, product usage, and device characteristics.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_SUBSCRIPTION]]
- ← [[CLM_CCM.CCM_SUBSCRIPTION_INFO_2]]
- ← [[CLM_CCM.CCM_PRODUCT_SUBSCRIPTION]]
- ← [[CLM_CCM.CCM_CUSTOMER]]
- ← [[CLM_CCM.CCM_CUSTOMER_INFO_2]]
- ← [[CLM_CCM.CCM_HOUSEHOLD_INFO]]
- ← [[CLM_CCM.CCM_FAR]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.HANDSET_DIM_V]]

