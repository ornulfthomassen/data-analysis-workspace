# VYA_CUSTOMER_INFO_HIST

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a historical snapshot of customer information, including demographic details (age, gender, birth month), household attributes (e.g., household address, unit, size), contact preferences (email, SMS indicators), address details (postal code, municipality, geographical area), and various service subscriptions (fixed telephony, TV, internet - DSL, WiMAX, Fiber, Dialup; mobile internet, mobile telephony). Its primary purpose is to cast most of these historical customer attributes into fixed-length character strings, likely for data standardization, reporting, or integration with external systems that require specific string formats.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]

