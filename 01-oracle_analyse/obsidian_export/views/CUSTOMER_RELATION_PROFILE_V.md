# CUSTOMER_RELATION_PROFILE_V

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a comprehensive, denormalized profile of customer relationships, including counts of various services (mobile, fixed, broadband, TV), associated flags (e.g., family bonus, secure ID), and customer status information. It combines raw profiling data with customer mapping information and converts date keys into proper date formats for easier consumption.

## Data Sources (Inputs)
- ← [[GALAXY.CUSTOMER_RELATION_PROFILE_FACT]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]

