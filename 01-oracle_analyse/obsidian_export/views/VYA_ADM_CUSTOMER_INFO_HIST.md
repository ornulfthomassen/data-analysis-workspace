# VYA_ADM_CUSTOMER_INFO_HIST

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a historical, monthly consolidated view of detailed customer and household demographic, consent, and geographical information. It combines data from core customer and household history tables, enriches it with derived segments (e.g., life stage), and applies specific filters to present a curated dataset, likely for analytical purposes or loading into downstream data systems (indicated by 'LOADING CUSTOMER_INFO_HIST-DATA TO MJØSA').

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_HOUSEHOLD_INFO_HIST]]

