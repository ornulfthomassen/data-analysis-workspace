# TEL_GIM_TRAFFIC_SKILL_SAS_VIEW

**Schema:** `CCM` | **Type:** `View`

## Description
This view serves as a direct, un-transformed projection of call center traffic and skill-related metrics and dimensions. It provides detailed data points such as call counts (offered, answered, lost), talk times, various wait times, after-work duration, transfer/consultation details, and callback counts, categorized by time dimensions (year, month, week, day) and operational attributes (virtual queue, client, program, type). The view is likely created to simplify access to the underlying data for reporting and analytical tools, potentially SAS, given its name, without applying any aggregations or complex transformations itself.

## Data Sources (Inputs)
- ← [[RSSHUGIN.TEL_GIM_TRAFFIC]]

