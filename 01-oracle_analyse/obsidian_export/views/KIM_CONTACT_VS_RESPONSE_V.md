# KIM_CONTACT_VS_RESPONSE_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates contact and response data, providing the minimum and maximum interaction dates and the total count of interactions for each 'SOURCE_SYSTEM_KEY'. It distinguishes between campaign contact details (labeled 'F') and customer responses (labeled 'R') by combining data from two different fact tables.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
- ← [[KIM_CUSTOMER_RESPONSE]]

