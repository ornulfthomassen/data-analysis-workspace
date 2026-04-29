# GCP_EMAIL_SUBSCRIPTION_INFO

**Schema:** `CCM` | **Type:** `View`

## Description
Retrieves active email subscriptions classified as 'Abonnement' that are not associated with an active 'Abonnementsavslutning' (subscription termination) add-on service. It extracts the subscription identifier and the trimmed email address.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SUBSCRIPTION_ID_VALUE |
| PRODUCT_OFFER_ID |
| CURRENT_STATUS |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_ACCESS_TYPE_NAME |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_MARKET_PRODUCT |
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PRODUCT_OFFER_ID |
| END_DATE |

