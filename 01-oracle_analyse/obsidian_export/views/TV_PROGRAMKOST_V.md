# TV_PROGRAMKOST_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates TV content product details with subscriber/usage base (UB/IB) information and various customer/product attributes. It derives a reporting period and applies specific business logic to categorize content segments based on product segment, unit price, and content segment from the joined tables. The view likely serves as a comprehensive data source for reporting and analysis related to TV program costs, subscriber metrics, and content performance.

## Data Sources (Inputs)
- ← [[CCM.TV_CONTENT_IB_UB_V]]
- ← [[QLIKVIEW.TV_CONTENT_PRODUCT_V]]

