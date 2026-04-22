# VYA_MK1727_CORE_REV

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a view of pre-calculated core revenue and usage (MB) metrics for subscriptions across multiple periods (e.g., M1, M2, M3, 3 Month Adjusted). It selects these metrics along with subscription key, period ID, active days, and days in period from its source, casting the subscription key to a CHAR(12) data type.

## Data Sources (Inputs)
- ← [[ADHOC_BS.MK_1727_RES]]

