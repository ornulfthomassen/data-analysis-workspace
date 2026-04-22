# KIM_RESPONSE_STG_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, 'KIM_RESPONSE_STG_V', consolidates and stages detailed information about customer responses to marketing campaigns. It joins raw campaign response data with customer and subscription mapping information to provide a comprehensive record of each response, including event timestamps, channel details, campaign attributes, and linked customer/subscription identifiers. The 'DISTINCT' clause ensures unique response records, and the naming convention suggests its use as an intermediary staging view for further processing or reporting related to Customer Interaction Management (KIM).

## Data Sources (Inputs)
- ← [[CLM_KIM.KIM_RESPONSE_STG]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]

