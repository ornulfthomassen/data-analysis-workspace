# KIM_CAMPAIGN_COMMUNICATION_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
This view serves as a dimension table that combines and enriches information from campaign and communication dimensions. It links individual communications to their respective campaigns, providing a consolidated view of campaign-communication attributes. A unique `CAMPAIGN_COMMUNICATION_KEY` is generated for each campaign-communication pair, making it suitable for analytical purposes.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_COMMUNICATION_DIM]]
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DIM]]

