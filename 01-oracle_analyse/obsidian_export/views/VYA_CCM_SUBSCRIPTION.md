# VYA_CCM_SUBSCRIPTION

**Schema:** `CCM` | **Type:** `View`

## Description
This view, VYA_CCM_SUBSCRIPTION, is designed to consolidate and present key subscription information, linking subscriptions to different customer roles (owner, user, and payer). It extracts core subscription details such as unique subscription and product identifiers, various start and end dates related to the subscription and its main product, and calculates the total days a subscription has been active. It maps the 'KURT_ID' from the subscription table to 'CUSTOMER_SK' for the owner, user, and payer roles, handling cases where a payer might not have a direct mapping.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_SUBSCRIPTION_V]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]

