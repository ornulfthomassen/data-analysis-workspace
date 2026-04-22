# VYA_SUBSCRIPTION_HISTORY

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a historical record of subscription details, including subscription identifiers, customer information, product details (brand, name, offer ID), market and business areas, and various duration metrics related to subscription activity (e.g., days active, days since last start/change, bind start/end days). It casts many numerical identifiers and keys to character strings of specific lengths, likely for data warehousing or reporting purposes.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]

