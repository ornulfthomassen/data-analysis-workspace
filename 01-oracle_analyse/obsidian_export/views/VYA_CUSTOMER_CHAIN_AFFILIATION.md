# VYA_CUSTOMER_CHAIN_AFFILIATION

**Schema:** `CCM` | **Type:** `View`

## Description
This view, VYA_CUSTOMER_CHAIN_AFFILIATION, is designed to extract and present aggregated customer affiliation data, tracking customer interactions with dealer chains and IDs over time, and associated Key Performance Indicators (KPIs). It provides details like the number of dealer chains/IDs a customer interacted with, the first and last order dates and corresponding dealer affiliations, and lists of all related order dates, dealer chains, and dealer IDs. It also includes various KPIs such as binding, newsale, porting, product changes, termination, and gross sales, both as individual values and lists. The view appears to serve as an intermediate step for loading CCM_PRODUCT_SUBSCRIPTION-data to the 'Mjøsa' system, likely for analytical purposes.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_CHAIN_AFFILIATION]]

