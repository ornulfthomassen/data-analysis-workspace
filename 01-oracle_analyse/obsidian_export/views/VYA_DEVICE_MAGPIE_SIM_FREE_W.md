# VYA_DEVICE_MAGPIE_SIM_FREE_W

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and standardizes weekly 'SIM-free' mobile device offers and their upfront costs collected from a third-party service (Magpie). It performs extensive data cleaning on device names and brands, calculates various price statistics (maximum, minimum, average, and median upfront costs), and attempts to map these devices to internal Global Trade Item Numbers (GTINs) using multiple matching strategies. The view filters out non-mobile phone devices (e.g., watches, tablets) and non-new conditions, focusing specifically on offers that are truly 'SIM-free' (zero effective monthly cost) and have a significant upfront cost. It enriches the data with weekly date dimensions for temporal analysis.

## Data Sources (Inputs)
- ← [[THIRD_PARTY_SERVICES.MAGPIE_DEVICE_PRICE]]
- ← [[FPS.TERMINAL_GTIN_PROPERTIES]]
- ← [[GALAXY.DATE_DIM_MV]]

